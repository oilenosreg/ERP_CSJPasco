from django.urls import path


from .views import ListUsersView, CreateUserView, create_user

app_name = 'users'
urlpatterns = [
    path('', ListUsersView.as_view(), name='list'),
    path('registro/<str:dni>/', create_user, name='create'),    
]
