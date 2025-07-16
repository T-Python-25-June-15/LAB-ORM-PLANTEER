from django.urls import path
from .views import plant_list_view, plant_create_view, plant_search_view, plant_detail_view, plant_update_view, plant_delete_view

app_name = 'plants'

urlpatterns = [
    path('all/', plant_list_view, name='plant_list'),
    path('new/', plant_create_view, name='plant_create'),
    path('search/', plant_search_view, name='search'),
    path('<int:plant_id>/detail/', plant_detail_view, name='plant_detail'),
    path('<int:plant_id>/update/', plant_update_view, name='plant_update'),
    path('<int:plant_id>/delete/', plant_delete_view, name='plant_delete'),


]
