from django.urls import path


from .views import ListUsersView, CreateUserView

app_name = 'users'
urlpatterns = [
    path('', ListUsersView.as_view(), name='list'),
    path('registro/', CreateUserView.as_view(), name='create'),    
]
