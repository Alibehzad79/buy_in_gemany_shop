from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account_app.models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass