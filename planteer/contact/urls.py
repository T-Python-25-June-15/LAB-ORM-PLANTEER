from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),  
    path('messages/', views.messages_from_users, name='messages_from_users'),  
]
