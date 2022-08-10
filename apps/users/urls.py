from django.contrib.auth import views as auth_views
from django.urls import path


from .views import (
    ListUsersView, register_user, create_user, CustomLoginView)


app_name = 'users'
urlpatterns = [
    path('', ListUsersView.as_view(), name='list'),
    path('nuevo/', create_user, name='create'),
    path('registro/<str:dni>/', register_user, name='register'),    
    path('ingresar/', CustomLoginView.as_view(), name='login'),
    path('salir/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), 
        name='logout'),
]
