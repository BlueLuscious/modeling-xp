from django.contrib import admin
# from ..forms import EntityChangeForm, EntityCreationForm
from ..models.talent_model import TalentProfile


@admin.register(TalentProfile)
class TalentModelAdmin(admin.ModelAdmin):

    # Forms
    # add_form = EntityCreationForm
    # form = EntityChangeForm

    list_display = ("agency", "height", "measurements", "portfolio_url",)
    search_fields = (
        "agency__client__entity__username", 
        "agency__client__entity__email", 
        "agency__client__company_name",
    )
    list_filter = ("agency",)

    # Edit User Form Layout
    fieldsets = (
        (None, {"fields": ("agency",)}),
        ("Talent profile", {"fields": ("bio", "height", "measurements", "portfolio_url")}),
        # ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),     
    )

    # Create User Form Layout
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("agency", "bio", "height", "measurements", "portfolio_url"),
        }),
    )

    def get_fields(self, request, obj = ...):
        return super().get_fields(request, obj)
