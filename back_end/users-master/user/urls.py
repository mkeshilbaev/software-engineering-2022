from rest_framework.urls import path

from user import views


urlpatterns = [
    path('', views.UserView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('check/', views.CheckAccessView.as_view())
]