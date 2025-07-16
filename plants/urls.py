from django.urls import path
from . import views as plants


app_name = 'plants'

urlpatterns = [
    path('all/', plants.all_plant_view, name='all_plants_view'),
    path('new/', plants.new_plant_view, name='new_plants_view'),
    path('<int:plant_id>/detail/', plants.detail_plant_view, name='detail_plant_view'),
    path('<int:plant_id>/delete/', plants.delete_plant, name='delete_plant'),
    path('<int:plant_id>/update/', plants.update_plant_view, name='update_plant_view'),
]
