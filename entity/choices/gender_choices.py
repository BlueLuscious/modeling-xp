from django.db.models import TextChoices

class GenderChoices(TextChoices): 
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"