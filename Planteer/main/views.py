from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from plants.models import Plant

# Home Page
def home_view (request: HttpRequest):

    plants = Plant.objects.all()[:3]

    return render (request, "main/index.html", context={"plants" : plants})


# Contact Page
def contact_view (request: HttpRequest):
    return render(request, "main/contact.html")


# Contact Messages Page
def contact_messages_view(request: HttpRequest):
    return render(request, "main/contact_messages.html")
