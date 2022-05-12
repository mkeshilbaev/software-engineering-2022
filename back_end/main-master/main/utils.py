import requests

from .models import Service


def callGetMethod(name, method):
    cur_service = Service.objects.get(name=name)
    data = cur_service.remote_call(method=method,)
    return data


# def change():
#     service = Service.objects.get(name='core')
#     print(service.url)
#     service.url = 'http://core:8000/'
#     service.save()
#     print(service.name, service.host, service.url)


# Service.objects.create(name='core',host='core.us',url='http://core:8000/')


def check_permission(user_id):
    cur_user = requests.post(url='http://user:8000/user/check/', data={'user_id': user_id})
    print(cur_user.json())
    return cur_user.json()