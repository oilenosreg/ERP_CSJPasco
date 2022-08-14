from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, AuthenticationForm)
from django import forms

# App modules.
from .models import CustomUser


class CreateUserForm(UserCreationForm):
    dni = forms.CharField(
        label='Nombre de usuario',
        max_length=8, 
        required=True, 
        help_text = 'Su número de DNI será su identificador de usuario para acceder al sistema.',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Número de DNI',                
                'class': 'form-control',}))
    password1 = forms.CharField(
        label='Clave de acceso',
        max_length=50, 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese su clave de acceso',
                'help_text': 'Su clave debe tener más de ocho caracteres, entre números, letras y símbolos.',
                'data-toggle': 'password',
                'class': 'form-control',
                'id': 'password', }))
    password2 = forms.CharField(
        label='Confirmación',
        max_length=50, 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirme su clave de acceso',
                'help_text': 'Confirme su clave de acceso.',
                'data-toggle': 'password',
                'class': 'form-control',
                'id': 'password', }))
    class Meta:
        model = CustomUser
        fields = ('dni', 'password1', 'password2',)
        # exclude = ('dni', )
        labels = {
            'dni': 'Nombre de usuario',
            'password1': 'Clave de acceso',
            'password2': 'Confirmar clave de acceso',
        }


class EditUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('dni', )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        max_length=8,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Número de DNI',
                'class': 'form-control',
                'data-toggle': 'DNI',
                'autocomplete': 'off',
                'id': 'dni',
                'name': 'dni',}))
    password = forms.CharField(
        label='Contraseña',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Clave de acceso',
                'class': 'form-control',
                'data-toggle': 'Clave de acceso',
                'id': 'password',
                'name': 'password',}))
    remember_me = forms.BooleanField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'remember_me']
