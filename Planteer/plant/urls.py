from django.urls import path
from . import views


app_name = "plant"

urlpatterns = [
    path("new/", views.add_plant_view, name="add_plant_view"),
    path("all/", views.all_plant_view, name="all_plant_view"),
    path("<plant_id>/detail/", views.details_view, name="details_view"),
    path("<plant_id>/update/", views.update_plant_view, name="update_plant_view"),
    path("<plant_id>/delete/", views.delete_plant_view, name="delete_plant_view"),
    path("search/", views.search_plant_view, name="search_plant_view"),
]