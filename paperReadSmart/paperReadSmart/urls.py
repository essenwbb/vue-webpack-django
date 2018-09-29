from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('data/', include('data.urls')),
    path(r'users/', include('users.urls')),
    path(r'users/', include('django.contrib.auth.urls')),
    path(r'', views.index, name='index'),
]