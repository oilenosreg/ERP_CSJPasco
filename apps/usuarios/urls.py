from django.urls import path


from .views import home

app_name = 'usuarios'
urlpatterns = [
    path('', home, name='home'),
]
