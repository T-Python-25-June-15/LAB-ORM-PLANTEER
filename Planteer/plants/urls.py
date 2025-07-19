from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [
    path("all/", views.all_plants_view, name="all_plants"),
    path("new/", views.add_plant, name="add_plant"),
    path("<int:plant_id>/detail/", views.plant_detail_view, name="plant_detail"),
    path('<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('review/<int:plant_id>/', views.add_review, name='add_review'),
    
]