from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path('add/' ,views.add_plant, name='add_plant') ,
    path("detail/<plant_id>/", views.plant_detail_view, name="plant_detail_view"),
    path("update/<plant_id>/", views.plant_update_view, name="plant_update_view"),
    path("delete/<plant_id>/", views.plant_delete_view, name="plant_delete_view"),
    path("all/", views.all_plant_view, name="all_plant_view"),
    path("search/", views.search_plants_view, name="search_plants_view"),
    path("reviews/add/<int:plant_id>/" , views.add_review_view , name= "add_review_view")
]