from django.urls import path

# App modules.
from .views import list_empleados, create_empleado, edit_empleado


app_name = 'employees'
urlpatterns = [
    path('', list_empleados, name='list'),
    path('nuevo/<str:dni>/', create_empleado, name='create'),
    path('modificar/<str:dni>/<int:id>/', edit_empleado, name='edit'),
]