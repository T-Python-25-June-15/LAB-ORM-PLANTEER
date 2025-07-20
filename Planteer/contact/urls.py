from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path("", views.create_form_contact, name='create_form_contact'),
    path("messages/", views.show_all_messages, name='show_all_messages'),
    path("delete/<int:message_id>/", views.delete_message, name='delete_message'),
]