from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("", views.home_view, name = "home_view"),
    path("contact/", views.contact_view, name = "contact_view"),
    path("contact/messages/", views.messages_view, name = "messages_view"),
    path("delete/<message_id>/", views.delete_message_view, name="delete_message_view"),

]