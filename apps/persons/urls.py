from django.urls import path

# App modules.
from .views import list_personas

app_name = 'persons'
urlpatterns = [
    path('', list_personas, name='list_personas'),
]