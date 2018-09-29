from django.urls import path

from . import views

app_name = 'data'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_life_gdp_data/', views.get_life_gdp_data, name='get_life_gdp_data')
]
