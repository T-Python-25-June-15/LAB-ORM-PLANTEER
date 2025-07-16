from django.shortcuts import render
from plants.models import Plant

# Create your views here.

def home_view(request):
    featured_plants = Plant.objects.all()[:3]  
    return render(request, 'main/home.html', {'featured_plants': featured_plants})

def contact_view(request):
    return render(request, 'main/contact.html')