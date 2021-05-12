from django import forms
from django.forms.models import model_to_dict
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'