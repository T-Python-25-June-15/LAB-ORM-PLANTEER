from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from plants.models import Plant

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    latest_plants = Plant.objects.order_by('-created_at')[:3]
    return render(request, 'main/index.html', {'latest_plants':latest_plants})
