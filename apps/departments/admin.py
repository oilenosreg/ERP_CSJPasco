from telnetlib import SE
from django.contrib import admin

# App modules.
from .models import (
    DistritoJudicial, SedeJudicial, ModuloCoordinacion,
    EdificioInstitucional, Dependencia)


admin.site.register(DistritoJudicial)
admin.site.register(SedeJudicial)
admin.site.register(ModuloCoordinacion)
admin.site.register(EdificioInstitucional)
admin.site.register(Dependencia)
