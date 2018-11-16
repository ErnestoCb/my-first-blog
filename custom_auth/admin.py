from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm()
    model = CustomUser
    list_display = ['run', 'email', 'pichula',]


admin.site.register(CustomUser, CustomUserAdmin)
