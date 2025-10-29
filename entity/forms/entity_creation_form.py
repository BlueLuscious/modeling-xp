# from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models.entity_model import EntityModel


class EntityCreationForm(UserCreationForm):
    """ Form for creating new instances of EntityModel in the admin or other views. """

    class Meta:
        model = EntityModel
        fields = "__all__"
