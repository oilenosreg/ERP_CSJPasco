from atexit import register
from django.contrib import admin

# Project modules.
from .models import Cargo, Empleado


admin.site.register(Cargo)
admin.site.register(Empleado)