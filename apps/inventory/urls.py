from django.urls import path

# App modules.
from .views import list_equipos, create_equipo


app_name = 'inventory'
urlpatterns = [
    path('equipos/', list_equipos, name='list_equipo'),
    path('equipos/nuevo/', create_equipo, name='create_equipo'),
]