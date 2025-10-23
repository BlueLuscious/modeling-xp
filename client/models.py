from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class roles(models.TextChoices):
        EMPRESARIO = 'EMPRESARIO', 'Empresario'
        MODELO = 'MODELO', 'Modelo'
        MODERADOR = 'MODERADOR', 'Moderador'
    role = models.CharField(
        max_length=10,
        choices=roles.choices,
        default=roles.MODELO,
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    # HELPERS
    @property
    def is_empresario(self): return self.role == self.Role.EMPRESARIO
    @property
    def is_modelo(self):     return self.role == self.Role.MODELO
    @property
    def is_moderador(self):  return self.role == self.Role.MODERADOR