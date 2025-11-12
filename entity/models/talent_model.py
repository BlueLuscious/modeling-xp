from django.db import models
from .entity_model import EntityModel
from .agency_model import AgencyModel

class TalentProfile(models.Model):
    entity = models.OneToOneField(
        EntityModel, on_delete=models.CASCADE, related_name="talent_profile"
    )
    bio = models.TextField(blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    measurements = models.CharField(max_length=255, blank=True)
    portfolio_url = models.URLField(blank=True)
    agency = models.ForeignKey(
        AgencyModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="talents"
    )

    def __str__(self):
        return f"Talent: {self.entity.username}"
