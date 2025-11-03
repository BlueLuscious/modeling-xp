from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class ShoeSizeSystem(models.TextChoices):
    US = "US", "US"
    EU = "EU", "EU"
    UK = "UK", "UK"


class GenderChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"
    NOT_SET = "N", "Prefer not to say"


class FitChoices(models.TextChoices):
    SHORT = "S", "Short"
    REGULAR = "R", "Regular"
    LONG = "L", "Long"


class HairColorChoices(models.TextChoices):
    BLACK = "blk", "Black"
    BROWN = "brn", "Brown"
    BLONDE = "bld", "Blonde"
    RED = "red", "Red"
    GREY = "gry", "Grey"
    OTHER = "oth", "Other"


class EyeColorChoices(models.TextChoices):
    BROWN = "brn", "Brown"
    BLUE = "blu", "Blue"
    GREEN = "grn", "Green"
    HAZEL = "hzl", "Hazel"
    GREY = "gry", "Grey"
    OTHER = "oth", "Other"

class EntityModel(AbstractUser):
    """ Custom User Model that extends Django's AbstractUser. """
    
    # Contacto / media
    phone_number = models.CharField(max_length=32, blank=True, default="")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    # Perfil público (de la captura)
    gender = models.CharField(
        max_length=1, choices=GenderChoices.choices, blank=True, default=GenderChoices.NOT_SET
    )

    # Altura: guardar en centímetros (evita '6\'1"').
    height_cm = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MinValueValidator(100), MaxValueValidator(250)],
        help_text="Altura en cm (ej. 185)"
    )

    # Traje: 38 R -> talla + calce (fit)
    suit_size = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MinValueValidator(30), MaxValueValidator(60)],
        help_text="Talla de saco (US), ej. 38"
    )
    suit_fit = models.CharField(
        max_length=1, choices=FitChoices.choices, blank=True, default=""
    )

    # Camisa: en la captura se ve '15.5/38'. Dividimos en cuello y manga.
    shirt_neck_in = models.DecimalField(  # pulgadas
        max_digits=4, decimal_places=1, blank=True, null=True,
        validators=[MinValueValidator(10), MaxValueValidator(20)],
        help_text='Cuello en pulgadas (ej. 15.5)'
    )
    shirt_sleeve_in = models.PositiveSmallIntegerField(  # pulgadas enteras (o cambia a Decimal si querés 0.5)
        blank=True, null=True, validators=[MinValueValidator(30), MaxValueValidator(40)],
        help_text='Largo de manga en pulgadas (ej. 38 = 38")'
    )

    # Pantalón
    waist_in = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True,
        validators=[MinValueValidator(20), MaxValueValidator(50)],
        help_text='Cintura en pulgadas'
    )
    inseam_in = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True,
        validators=[MinValueValidator(20), MaxValueValidator(40)],
        help_text='Tiro interior (inseam) en pulgadas'
    )

    # Calzado
    shoe_size = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True,
        validators=[MinValueValidator(3), MaxValueValidator(50)]
    )
    shoe_size_system = models.CharField(
        max_length=2, choices=ShoeSizeSystem.choices, blank=True, default=ShoeSizeSystem.US
    )

    # Apariencia
    hair_color = models.CharField(max_length=3, choices=HairColorChoices.choices, blank=True, default="")
    eye_color = models.CharField(max_length=3, choices=EyeColorChoices.choices, blank=True, default="")

    # Sindicato (Union)
    union_member = models.BooleanField(default=False)

    # Ubicación (Los Angeles, CA)
    city = models.CharField(max_length=64, blank=True, default="")
    region = models.CharField(max_length=64, blank=True, default="")  # estado/provincia
    country = models.CharField(max_length=64, blank=True, default="")

    # Tarifas (USD, por lo que se ve)
    rate_hourly_usd = models.PositiveIntegerField(blank=True, null=True)  # ej. 250
    rate_daily_usd = models.PositiveIntegerField(blank=True, null=True)   # ej. 1800

    # Señales de actividad/perfil
    experienced = models.BooleanField(default=False)      # la "badge" EXPERIENCED
    last_seen_at = models.DateTimeField(blank=True, null=True)  # "Online 1d ago"
    response_time_avg_min = models.PositiveSmallIntegerField(blank=True, null=True)  # "within an hour"

    # Otros
    metadata = models.JSONField(default=dict, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ---- Helpers (opcional, solo presentación) ----
    @property
    def height_feet_inches(self) -> str | None:
        if not self.height_cm:
            return None
        total_in = round(self.height_cm / 2.54)
        feet, inches = divmod(total_in, 12)
        return f"{feet}'{inches}\""

    @property
    def suit_display(self) -> str:
        if self.suit_size and self.suit_fit:
            return f"{self.suit_size} {self.get_suit_fit_display()}"
        return str(self.suit_size or "")

    @property
    def shirt_display(self) -> str:
        if self.shirt_neck_in and self.shirt_sleeve_in:
            return f"{self.shirt_neck_in}/{self.shirt_sleeve_in}"
        return str(self.shirt_neck_in or "")


    # Models fields antes del nuevo cambio que propuso ChatGTP

    # phone_number = models.CharField(max_length=32, default="", blank=True)
    # avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    # metadata = models.JSONField(default=dict, blank=True)
    # Gender = models.CharField(max_length=16, blank=True)
    # Height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # suit = models.CharField(max_length=64, blank=True)
    # shirt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # Waist = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # Inseam = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # Shoes = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # hair = models.CharField(max_length=64, blank=True)
    # eyes = models.CharField(max_length=64, blank=True)
    # union = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
  
    # @property
    # def roles(self) -> list[str]:
    #     """ Get a list of a user's roles. """
    #     return list(self.groups.values_list("name", flat=True))

    # @property
    # def roles_label(self) -> str:
    #     """ Retrieves all the names of a user's roles concatenated into a string. """
    #     return " | ".join(self.roles) if self.roles else "Sin rol"

    # @property
    # def is_agency(self) -> bool:
    #     """ Check if the user belongs to the 'Agency' group. """
    #     return self.groups.filter(name="Agency").exists()

    # @property
    # def is_client(self) -> bool:
    #     """ Check if the user belongs to the 'Client' group. """
    #     return self.groups.filter(name="Client").exists()

    # def __str__(self) -> str:
    #     return f"{self.username} ({self.roles or 'Sin rol'})"
