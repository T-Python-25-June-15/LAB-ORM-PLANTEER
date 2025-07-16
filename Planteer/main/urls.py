from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home_views, name="home_views"),
    path('contact/',views.contact_us_views, name="contact_us_views"),
]