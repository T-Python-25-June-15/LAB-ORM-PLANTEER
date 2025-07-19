from . import views
from django.urls import path
from . import views


app_name= 'main'
urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('contactus/', views.contact_us_view, name="contact_us_view"),
    path('contactus/messages', views.contact_us_messages_view, name="contact_us_messages_view")
]