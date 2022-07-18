from django.urls import path

# App modules.
from .views import listar_equipos, create_equipo, edit_equipo, detail_equipo, asignar_equipo


app_name = 'inventory'
urlpatterns = [
    path('equipos/', listar_equipos, name='listar_equipos'),
    path('equipos/nuevo/', create_equipo, name='create_equipo'),
    path('equipos/modificar/<int:id>', edit_equipo, name='edit_equipo'),
    path('equipos/detalle/<int:id>/', detail_equipo, name='detail_equipo'),
    path('equipos/<int:id>/asignar/', asignar_equipo, name='asignar_equipo'),
]