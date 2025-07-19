from django.urls import path
from . import views

app_name = "plant"

urlpatterns = [
    path("new/",views.newPlant_view, name="newPlant_view"),
    path("all/", views.AllPlant_view, name="AllPlant_view"),
    path("<plant_id>/detail/", views.detail_view, name="detail_view"),
    path("<plant_id>/update/", views.update_view, name="update_view"),
    path("<plant_id>/delete/",views.delete_view, name="delete_view"),
    path("search/", views.search_view, name="search_view"),
    path("comments/add/<plant_id>", views.add_comment_view, name="add_comment_view"),
]