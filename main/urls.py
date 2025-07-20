from django.urls import path
from .views import home_view
from .views import contact_view
from .views import contact_messages_view

app_name = "main"

urlpatterns = [
    path('', home_view, name='home_view'),
    path('contact/', contact_view, name='contact_view'),
    path('contact/messages/', contact_messages_view, name='contact_messages_view'),
] 