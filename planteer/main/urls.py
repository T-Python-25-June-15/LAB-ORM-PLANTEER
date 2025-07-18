from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/messages/', views.contact_messages_view, name='contact_messages'),
    path('contact/messages/<int:pk>/delete/', views.delete_contact_message, name='delete_contact_message'),
]


