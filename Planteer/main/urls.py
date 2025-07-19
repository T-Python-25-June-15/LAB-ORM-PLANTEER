from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('plants/search/', views.search_view, name='search'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/messages/', views.messages_view, name='messages'),
]