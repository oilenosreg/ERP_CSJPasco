from django.urls import path


from .views import (
    ListUsersView, CreateUserView, register_user, create_user)


app_name = 'users'
urlpatterns = [
    path('', ListUsersView.as_view(), name='list'),
    path('nuevo/', create_user, name='create'),
    path('registro/<str:dni>/', register_user, name='register'),    
]
