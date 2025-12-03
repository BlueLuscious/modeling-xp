from django.contrib import admin
from ..forms import EntityChangeForm, EntityCreationForm
from ..models.agency_model import AgencyModel


@admin.register(AgencyModel)
class AgencyModelAdmin(admin.ModelAdmin):
    """ Admin panel for the ClientModel custom user. """

    # Forms
    # add_form = EntityCreationForm
    # form = EntityChangeForm

    list_display = ("client", "verified", "description",)
    ordering = ("client__entity__username",)
    search_fields = ("client__entity__username", "client__company_name", "client__entity__email",)
    list_filter = ("verified",)

    # Edit User Form Layout
    fieldsets = (
        ("user", {"fields": ("client",)}),
        ("Agency details", {"fields": ("verified", "description")}),
        # ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),     
    )

    # Create User Form Layout
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("client", "verified", "description",),
        }),
    )
