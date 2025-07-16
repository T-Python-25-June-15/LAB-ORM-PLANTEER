from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path('new/',views.add_views, name="add_views"),
    path('all/',views.all_views, name="all_views"),
    path('<plant_id>/detail/', views.details_views, name="details_views"),
    path('<plant_id>/update/',views.update_views, name="update_views"),
    path('<plant_id>/delete/',views.delete_views, name="delete_views"),
    path('search/',views.search_views, name="search_views"),
    path('comment/add/<plant_id>/', views.comment_views, name="comment_views"),
]