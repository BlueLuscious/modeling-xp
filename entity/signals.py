from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.entity_model import EntityModel
from .models.client_model import ClientProfile
from .models.talent_model import TalentProfile

@receiver(post_save, sender=EntityModel)
def create_related_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.type == "model":
            TalentProfile.objects.create(entity=instance)
        elif instance.type == "client":
            ClientProfile.objects.create(entity=instance)
