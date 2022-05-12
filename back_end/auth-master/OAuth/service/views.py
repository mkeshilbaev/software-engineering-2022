from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework import mixins, viewsets

from OAuth.service.models import MyUser
from OAuth.service.serializer import UserShortSerializer, UserListSerializer

from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes

from OAuth.service.tasks import send_notification


class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserShortSerializer


class Validation(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserShortSerializer

    def get(self, request, *args, **kwargs):
        if request.user != '':
            return Response(data={'user_id': request.user.id}, status=status.HTTP_200_OK)


class is_valid_jwt(mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserShortSerializer


def validateUser(token):
    try:
        data = {'token': token}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        user = valid_data['user']

        return user.id
    except ValidationError as v:
        return "validation error"


class UserListView(mixins.ListModelMixin,
                   viewsets.GenericViewSet,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin):
    queryset = MyUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        else:
            return UserShortSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsAdminUser, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(kwargs['pk'])
        print(request.user.id)
        if kwargs['pk'] == str(request.user.id):
            return Response(serializer.data)
        else:
            return HttpResponseForbidden()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if kwargs['pk'] == str(request.user.id):
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponseForbidden()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if kwargs['pk'] == str(request.user.id):
            self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        if kwargs['pk'] == str(request.user.id):
            return Response(serializer.data)
        else:
            return HttpResponseForbidden()


@csrf_exempt
def password_reset_request(request):
    print(request.method)
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            print(data)
            associated_users = MyUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = 'password_reset_email.txt'
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8500',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    print(email)
                    try:
                        send_notification(subject, email, [user.email])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/auth/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html",
                  context={"password_reset_form": password_reset_form})
