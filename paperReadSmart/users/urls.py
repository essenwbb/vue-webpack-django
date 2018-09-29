from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path(r'register/', views.register, name='register'),
    path(r'write/', views.write, name='write'),
]