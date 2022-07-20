from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models

# App modules.
from .managers import UsuarioPersonalizadoManager


class Usuario(AbstractBaseUser, PermissionsMixin):
        dni = models.CharField('DNI', max_length=8, unique=True)
        
        is_staff = models.BooleanField(default=False)
        is_active = models.BooelanField(default=True)
        date_joined = models.DateTimeField(default=timezone.now)

        USERNAME_FIELD = 'dni'
        REQUIRED_FIELDS = []

        objects = UsuarioPersonalizadoManager()

        def __str__(self):
            return self.dni

            