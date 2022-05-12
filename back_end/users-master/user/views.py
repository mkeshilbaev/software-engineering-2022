from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer, CheckAccessSerializer


class UserView(generics.ListCreateAPIView):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CheckAccessView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CheckAccessSerializer