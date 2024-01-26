from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from AppDeco.models import *

class EspejoFormulario(forms.ModelForm):
    class Meta:
        model = Espejo
        fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'precio', 'imagen']

class SillonFormulario(forms.ModelForm):
    class Meta:
        model = Sillon
        fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'precio', 'imagen']

class LamparaFormulario(forms.ModelForm):
    class Meta:
        model = Lampara
        fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'colorluz', 'precio', 'imagen']

class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
