from django.urls import path
from . import views
from plants import views
from contact import views as contact_views
from django.urls import include


urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all_plants, name='all_plant'),
    path('plants/<int:plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('add_plant', views.add_plant, name='add_plant'),
    path('plants/<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('plants/<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('search/', views.search_plant, name='search'),
    path('reviews/<int:plant_id>/add/', views.add_review, name='add_review'),
]
