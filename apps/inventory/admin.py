from django.contrib import admin

#App modules.
from .models import Categoria, Marca, Modelo, Equipo, EquipoAsignado


class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nombre', 'subcategoria_de_id', 'activo', 'componentes', 'observaciones'
    ]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Equipo)
admin.site.register(EquipoAsignado)

