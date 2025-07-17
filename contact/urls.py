from django.urls import path
from . import views as contact

urlpatterns = [
    path('', contact.contact_view, name='contact_view'),
]
