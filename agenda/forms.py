from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario:")
    password = forms.CharField(label="Contraseña:", widget=forms.PasswordInput())


class MessageForm(forms.Form):
    issue = forms.CharField(label="Asunto", widget=forms.TextInput({
        'placeholder': 'Ingresa el asunto'
    }))
    content = forms.CharField(label="Contenido", widget=forms.Textarea({
        'placeholder': 'Ingresa tu mensaje'
    }))