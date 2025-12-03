from django.db import models
from .entity_model import EntityModel

class ClientProfile(models.Model):
    CLIENT_TYPES = [
        ("person", "Person"),
        ("agency", "Agency"),
    ]
    entity = models.OneToOneField(
        EntityModel, on_delete=models.CASCADE, related_name="client_profile"
    )
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPES)
    industry = models.CharField(max_length=255, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Client: {self.entity.username} ({self.get_client_type_display()})"
