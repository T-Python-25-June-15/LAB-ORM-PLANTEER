from django.urls import path
from . import views

app_name= 'plants'

urlpatterns= [
    path("all/", views.display_all_plants, name='display_all_plants'),
    path("new/", views.create_new_plant, name= 'create_new_plant'),
    path("search/", views.search_plant, name='search_plant'),
    path("<int:plant_id>/details/", views.show_plant_details, name='show_plant_details'),
    path("<int:plant_id>/delete", views.delete_plant, name='delete_plant' ),
    path("<int:plant_id>/update", views.update_plant, name='update_plant'),
]
