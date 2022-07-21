from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

# App modules.
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    dni = forms.CharField(
        max_length=8, required=True, widget=forms.TextInput(attrs={
            'placeholder': 'Número de DNI',
            'help_text': 'Su número de DNI será su identificador de usuario para acceder al sistema.',
            'class': 'form-control', }))
    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(attrs={
            'placeholder': 'Ingrese su clave de acceso',
            'help_text': 'Su clave debe tener más de ocho caracteres, entre números, letras y símbolos.',
            'data-toggle': 'password',
            'class': 'form-control',
            'id': 'password', }))
    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme su clave de acceso',
            'help_text': 'Confirme su clave de acceso.',
            'data-toggle': 'password',
            'class': 'form-control',
            'id': 'password', }))
    class Meta:
        model = Usuario
        # fields = ('dni', )
        fields = ['dni', 'password1', 'password2']


class EditarUsuarioForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('dni', )