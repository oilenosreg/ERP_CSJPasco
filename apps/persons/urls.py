from django.urls import path

# App modules.
from .views import list_personas, create_persona, edit_persona, profile_persona 

app_name = 'persons'
urlpatterns = [
    path('', list_personas, name='list'),
    path('nuevo/', create_persona, name='create'),
    path('modificar/<str:dni>/', edit_persona, name='edit'),
    path('perfil/<str:dni>/', profile_persona, name='profile'),
]