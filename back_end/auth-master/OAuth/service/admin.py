from django.contrib import admin

# Register your models here.
from django.contrib import admin

from OAuth.service.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'date_joined')
