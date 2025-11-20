from django.contrib import admin
from ..forms import EntityChangeForm, EntityCreationForm
from ..models.client_model import ClientProfile


@admin.register(ClientProfile)
class ClientModelAdmin(admin.ModelAdmin):
    """ Admin panel for the ClientModel custom user. """

    # Forms
    # add_form = EntityCreationForm
    # form = EntityChangeForm

    list_display = ("entity", "client_type", "company_name", "industry", "phone", "website",)
    ordering = ("entity__username",)
    search_fields = ("entity__username", "entity__email", "company_name", "industry", "phone",)
    list_filter = ("client_type", "industry")

    # Edit User Form Layout
    fieldsets = (
        ("Client type", {"fields": ("client_type",)}),
        ("User", {"fields": ("entity",)}),
        ("Customer/agency data", {"fields": ("industry", "company_name", "website", "phone",)}),
        # ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    # Create User Form Layout
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("entity", "client_type", "industry", "company_name", "website", "phone"),
        }),
    )
