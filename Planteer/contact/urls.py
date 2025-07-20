from django.urls import path
from . import views



app_name= "contact"

urlpatterns= [
    path('', views.contact_form_view, name="contact_form_view"),
    path('messages/', views.contact_messages_view, name="contact_messages_view"),
]