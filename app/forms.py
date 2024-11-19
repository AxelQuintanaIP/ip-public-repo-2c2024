# Aca desarrollamos todo lo necesario para la creacionde nuevos usuarios

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # con estas variables manejamos lo que queremos mostrar en el formulario para tener un mejor control del mismo
    username = forms.CharField(
        label = 'Nombre de Usuario',
        required=True,
    )
    first_name = forms.CharField(
        label = 'Nombre',
        required=False,
    )
    last_name = forms.CharField(
        label='Apellido',
        required=False,
    )
    email = forms.EmailField(
        label= 'Correo Electronico',
        required=True,
    )
    password1 = forms.CharField(widget=forms.PasswordInput, # agregamos un widget para que no se muestre la password con caracteres, sino con asteriscos
        label = "Contraseña",
        required=True
    )
    password2 = forms.CharField(widget=forms.PasswordInput,
        label = "Confirmar Contraseña",
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']