from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..forms import EntityChangeForm, EntityCreationForm
from ..models.entity_model import EntityModel


@admin.register(EntityModel)
class EntityModelAdmin(UserAdmin):
    """ Admin panel for the EntityModel custom user. """

    # Forms
    add_form = EntityCreationForm
    form = EntityChangeForm

    list_display = ("pk", "username", "first_name", "last_name", "created_at", "updated_at", "roles_label", )
    ordering = ("-created_at", )
    search_fields = ("username", "first_name", "last_name", )
    list_filter = ("groups__name", "is_staff", "is_active", )

    # Edit User Form Layout
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "phone_number", "avatar", "metadata")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Create User Form Layout
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "password1", "password2", "groups"),
        }),
    )
    