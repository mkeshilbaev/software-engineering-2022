from django.db import models

import requests, json


class Service(models.Model):
    name = models.CharField(
        unique=True,
        editable=True,
        max_length=100,
        help_text="Name of the service."
    )
    host = models.URLField(
        unique=True,
        editable=True,
        help_text="Host of the service. Ex. auth.example.com"
    )

    url = models.URLField(
        editable=True,
        help_text="URL of the proxy to the serviceess"
    )

    class Meta:
        ordering = ['name', 'host']

    def remote_call(self, request, headers):
        headers = headers
        print(headers)
        strip = '/main/'
        full_path = request.get_full_path()[len(strip):]
        url = self.url + full_path+'/'
        print(url)
        method = request.method.lower()
        print(method)
        method_map = {
            'get': requests.get,
            'post': requests.post,
            'put': requests.put,
            'patch': requests.patch,
            'delete': requests.delete
        }

        for k, v in request.FILES.items():
            request.data.pop(k)

        if request.content_type and request.content_type.lower() == 'application/json':
            data = json.dumps(request.data)
            headers['content-type'] = request.content_type
        else:
            data = request.data

        return method_map[method](url=url, headers=headers, data=data, files=request.FILES)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

