from django.db import models
from .client_model import ClientProfile

class AgencyModel(models.Model):
    client = models.OneToOneField(
        ClientProfile, on_delete=models.CASCADE, related_name="agency_data"
    )
    verified = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Agency: {self.client.company_name or self.client.entity.username}"