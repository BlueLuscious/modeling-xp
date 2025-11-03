from django.contrib.auth.models import AbstractUser
from django.db import models


class EntityModel(AbstractUser):
    """ Custom User Model that extends Django's AbstractUser. """
    
    phone_number = models.CharField(max_length=32, default="", blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def roles(self) -> list[str]:
        """ Get a list of a user's roles. """
        return list(self.groups.values_list("name", flat=True))

    @property
    def roles_label(self) -> str:
        """ Retrieves all the names of a user's roles concatenated into a string. """
        return " | ".join(self.roles) if self.roles else "Sin rol"

    @property
    def is_agency(self) -> bool:
        """ Check if the user belongs to the 'Agency' group. """
        return self.groups.filter(name="Agency").exists()

    @property
    def is_client(self) -> bool:
        """ Check if the user belongs to the 'Client' group. """
        return self.groups.filter(name="Client").exists()

    def __str__(self) -> str:
        return f"{self.username} ({self.roles or 'Sin rol'})"
