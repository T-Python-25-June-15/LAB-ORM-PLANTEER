from django.urls import path
from . import views as contact

app_name = 'contact'
urlpatterns = [
    path('', contact.contact_view, name='contact_view'),
    path('messages/', contact.all_contact, name='all_contact')
]
