from django.urls import path
from . import views

app_name = 'plant'

urlpatterns = [
path('plants/all/', views.all_plants_view, name='all_plants_view'),
path('plants/new/', views.add_plant_view, name='add_plant_view'),
path('plants/<int:plant_id>/detail/', views.plant_detail_view, name='plant_detail_view'),
path('plants/<int:plant_id>/update/', views.plant_update_view, name='plant_update_view'),
path('plants/<int:plant_id>/delete/', views.plant_delete_view, name='plant_delete_view'),
path('plants/search/', views.search_plant_view, name='search_plant_view'),
path('plants/comment/add/<int:plant_id>/', views.add_comment_view, name='add_comment_view'),

]