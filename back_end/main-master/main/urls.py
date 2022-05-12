from django.conf.urls import url, include
from django.urls import path
from main import views

urlpatterns = [
    url(r'.*', views.gateway.as_view()),
]
