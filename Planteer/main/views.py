from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plant.models import Plant
# Create your views here.

def home_view(request:HttpRequest):

    plants = Plant.objects.all()[0:3]


    return render(request, "home.html", {'plants':plants})

