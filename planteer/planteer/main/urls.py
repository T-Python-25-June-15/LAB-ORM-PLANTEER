from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
]
# The home view will be the landing page of the application.
# It can be used to display a welcome message, navigation links, or any other relevant information