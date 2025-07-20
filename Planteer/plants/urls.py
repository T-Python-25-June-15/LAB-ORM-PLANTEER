from django.urls import path
from . import views



app_name= "plants"

urlpatterns= [
    path("new/", views.create_plant_view, name="create_plant_view"),
    path("<plant_id>/detail/", views.detail_plant_view, name="detail_plant_view"),
    path("<plant_id>/update/", views.update_plant_view, name="update_plant_view"),
    path("<plant_id>/delete/", views.delete_plant_view, name="delete_plant_view"),
    path('all/', views.all_plant_view, name="all_plant_view"),
    path("search/", views.search_plants_view, name="search_plants_view")
    
]