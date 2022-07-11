from django.urls import path

# App modules.
from .views import list_personas, create_persona

app_name = 'persons'
urlpatterns = [
    path('', list_personas, name='list'),
    path('nuevo/', create_persona, name='create'),
]