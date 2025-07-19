from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plant.models import Plant
from .forms import ContactForm
# Create your views here.

def home_view(request:HttpRequest):

    plants = Plant.objects.all()[0:3]
    return render(request, "home.html", {'plants':plants})

def contact_view(request:HttpRequest):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("main:contact_view")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form":form})

