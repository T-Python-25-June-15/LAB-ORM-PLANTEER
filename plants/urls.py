from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('contact/messages/', views.contact_messages_view, name='contact_messages_view'),
    path('contact/messages/delete/<int:pk>/', views.contact_message_delete, name='contact_message_delete'),

    
]