from django.forms import ModelForm, EmailField, CharField
from .models import Carro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class CarroForm(ModelForm):
   
    class Meta:
        model=Carro
        fields='__all__'