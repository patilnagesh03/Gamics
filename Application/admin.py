from django.contrib import admin
from .models import UserRegister

# Register your models here.
@admin.register(UserRegister)
class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)