# from django import forms
from django.contrib.auth.forms import UserChangeForm
from ..models.entity_model import EntityModel


class EntityChangeForm(UserChangeForm):
    """ Form for updating instances of EntityModel in the admin or other views. """

    class Meta:
        model = EntityModel
        fields = "__all__"
