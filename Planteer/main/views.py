from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plants
# Create your views here.

def home_views(request:HttpRequest):
    plants = Plants.objects.all().order_by("-created_at")[0:3]
    return render(request, 'main/home.html', {"plants":plants} )


def contact_us_views(request:HttpRequest):
    return render(request, 'main/contact.html')