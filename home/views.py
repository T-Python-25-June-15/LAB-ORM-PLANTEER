from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse

from plants.models import Plant

# Create your views here.

def home_view(request:HttpRequest):
    plants = Plant.objects.all()[0:3]
    return render(request, 'home/index.html', {'plants': plants})

def search_view(request:HttpRequest):
    if request.method == 'POST':
        if 'search' in request.POST:
            plants_results = Plant.objects.filter(name__icontains = request.POST['search'])
            return render(request, 'home/search.html', {'plants': plants_results, 'search': request.POST['search']})
    return render(request, 'home/search.html')