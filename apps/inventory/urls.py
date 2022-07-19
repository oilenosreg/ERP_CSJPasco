from django.urls import path

# App modules.
from .views import listar_equipos, nuevo_equipo, editar_equipo, detail_equipo, asignar_equipo


app_name = 'inventory'
urlpatterns = [
    path('equipos/', listar_equipos, name='listar_equipos'),
    path('equipos/nuevo/', nuevo_equipo, name='nuevo_equipo'),
    path('equipos/<int:id>/modificar/', editar_equipo, name='editar_equipo'),
    path('equipos/<int:id>/detalle/', detail_equipo, name='detail_equipo'),
    path('equipos/<int:id>/asignar/', asignar_equipo, name='asignar_equipo'),
]