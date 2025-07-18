from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
  path('all/', views.plants_all, name="plants_all"),
  path('<int:plant_id>/detail/', views.plants_detail, name="plants_detail"),
  path('new/', views.plants_new, name="plants_new"),
  path('<int:plant_id>/update/', views.plants_update, name="plants_update"),
  path('<int:plant_id>/delete/', views.plants_delete, name="plants_delete"),
  path('search/', views.plants_search, name="plants_search"),

]