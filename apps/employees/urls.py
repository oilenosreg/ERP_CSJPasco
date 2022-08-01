from django.urls import path

# App modules.
from .views import (
    list_empleados, create_empleado, edit_empleado, list_departments)


app_name = 'employees'
# TODO: ordenar las url, dni primero?
urlpatterns = [
    path('', list_empleados, name='list'),
    path('<str:dni>/nuevo/cargo/', create_empleado, name='create'),
    path('modificar/<str:dni>/<int:id>/', edit_empleado, name='edit'),
    path('<str:dni>/cargos/', list_departments, name='list_departments'),
]