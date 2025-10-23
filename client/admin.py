from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # columnas de lista
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff", "is_active")
    list_filter  = ("role", "is_staff", "is_superuser", "is_active", "groups")
    # incluir "role" en los fieldsets del admin
    fieldsets = UserAdmin.fieldsets + (
        ("Rol", {"fields": ("role",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Rol", {"fields": ("role",)}),
    )