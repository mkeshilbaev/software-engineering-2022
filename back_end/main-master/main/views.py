import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateResponseMixin

from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header

from .models import Service
from .serializers import MicroServiceSerializer
from .utils import check_permission


class gateway(APIView, TemplateResponseMixin):
    authentication_classes = ()
    # renderer_class = (BrowsableAPIRenderer,)
    # content_type = 'text/html'

    def operation(self, request):
        headers = {}
        auth = get_authorization_header(request).split()
        if len(auth) == 2:
            print(auth[1].decode())
            key = auth[1].decode()
            headers = {'Authorization': 'jwt {key}'.format(key=key)}
        path = request.path_info.split('/')
        print(path)
        if len(path) < 2:
            return Response('bad request', status=status.HTTP_400_BAD_REQUEST)

        try:
            apimodel = Service.objects.get(name=path[2])
        except Exception as e:
            print(e)
            return Response('bad request', status=status.HTTP_400_BAD_REQUEST)

        # valid, msg = apimodel[0].check_plugin(request)
        # if not valid:
        #     return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        res = apimodel.remote_call(request=request, headers=headers)
        if res.headers.get('Content-Type', '').lower() == 'application/json':
            data = res.json()
            return Response(data=data, status=res.status_code)
        else:
            data = res.content
            return HttpResponse(content={data: data}, status=res.status_code)

    def get(self, request):
        return self.operation(request)

    def post(self, request):
        return self.check_access(request)

    def put(self, request):
        return self.check_access(request)

    def patch(self, request):
        return self.operation(request)

    def delete(self, request):
        return self.check_access(request)

    def check_access(self, request):
        try:
            user_id = request.data.pop('user_id')
            cur_user = check_permission(user_id=user_id)
            if cur_user['is_admin'] or cur_user['is_teacher']:
                print('Have access !!!!!!!!')
                return self.operation(request)
            return Response(data='Dont have access!!!', status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            print(e)
            return self.operation(request)


class ServiceView(generics.ListCreateAPIView):
    authentication_classes = (AllowAny, )
    serializer_class = MicroServiceSerializer
