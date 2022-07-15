from django.urls import path

# App modules.
from .views import list_equipos, create_equipo, edit_equipo


app_name = 'inventory'
urlpatterns = [
    path('equipos/', list_equipos, name='list_equipos'),
    path('equipos/nuevo/', create_equipo, name='create_equipo'),
    path('equipos/modificar/<int:id>', edit_equipo, name='edit_equipo'),
]