from django.urls import path


from .views import home, RegistroUsuarioView

app_name = 'usuarios'
urlpatterns = [
    path('', home, name='home'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),    
]
