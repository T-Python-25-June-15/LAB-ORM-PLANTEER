from django.urls import path
from . import views as home

app_name = 'home'

urlpatterns = [
    path('', home.home_view, name='home_view'),
    path('search/', home.search_view, name='search_view'),
]
