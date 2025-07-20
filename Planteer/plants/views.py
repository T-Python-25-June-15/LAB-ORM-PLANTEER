from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
from .forms import PlantForm

# Create your views here.

def display_all_plants(request: HttpRequest) -> HttpResponse:
    all_plants = Plant.objects.all()
    return render(request, 'plants/display_all_plants.html', context={'all_plants':all_plants})


def create_new_plant(request: HttpRequest) -> HttpResponse:
    plant_form = PlantForm()
    if request.method == 'POST':
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:display_all_plants')
        
        
    return render(request, 'plants/new_plant.html', {'plant_form':plant_form, 'CategoryChoices':Plant.CategoryChoices.choices})



def search_plant(request:HttpRequest) -> HttpResponse:
    query = request.GET.get('search')
    search_result = Plant.objects.filter(name__icontains= query) 
    return render(request, 'plants/search_plant.html', {'search_result':search_result})



def show_plant_details(request: HttpRequest, plant_id) -> HttpResponse:
    plant = Plant.objects.get(pk=plant_id)
    same_cat = Plant.objects.filter(category__icontains=plant.category).exclude(pk=plant_id)
    return render(request, 'plants/plant_details.html', {'plant':plant, 'same_cat':same_cat})



def delete_plant(request: HttpRequest, plant_id) -> HttpResponse:
    plant = Plant.objects.get(pk=plant_id)    
    plant.delete()
    return redirect('plants:display_all_plants')



def update_plant(request: HttpRequest, plant_id) -> HttpResponse:
    plant = Plant.objects.get(pk=plant_id)
    if request.method == 'POST':
        plant_form = PlantForm(request.POST, request.FILES, instance=plant)
        if plant_form.is_valid():      
            plant_form.save()
            return redirect('plants:show_plant_details',plant_id)
        
    return render(request, 'plants/update_plant.html', {'plant':plant, 'CategoryChoices':Plant.CategoryChoices.choices})

    


