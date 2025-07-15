from django.urls import path
from . import views


app_name = "plant"

urlpatterns = [
    path("create/", views.add_plant_view, name="add_plant_view"),
    path("all/plants", views.all_plant_view, name="all_plant_view"),
]