from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from OAuth.service.views import UserCreateView, UserListView, is_valid_jwt, Validation, password_reset_request
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'users', UserListView,)

urlpatterns = [

    path('register/', UserCreateView.as_view()),
    path('user', UserListView),
    path('jwt-validation/', Validation.as_view()),
    path('login/', obtain_jwt_token),
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete')
    #path('auth/',include('rest_framework_social_oauth2.urls')),

]
urlpatterns=urlpatterns+router.urls
