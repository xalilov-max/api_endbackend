# account/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_instructor', 'is_staff', 'is_active']  # Qaysi maydonlar ko'rsatilishini tanlang
    list_filter = ['is_instructor', 'is_staff', 'is_active']  # Filtrlash maydonlari
    search_fields = ['username', 'email']  # Qidirish maydonlari
    ordering = ['username']  # Tartiblash maydoni

admin.site.register(CustomUser, CustomUserAdmin)
