from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plants
from .forms import PlantForm

# Create your views here.

def all_plants_view(request:HttpRequest):
    plant_form = PlantForm()
    plants = Plants.objects.all()

    category = request.GET.get("category", "")
    is_edible = request.GET.get("is_edible", "")

    if category:
        plants = plants.filter(category=category)

    if is_edible in ["True", "False"]:
        plants = plants.filter(is_edible=(is_edible == "True"))

    return render(request,"plants/all_plants.html", {"plants" : plants, "plant_form" : plant_form})

def plant_detail_view(request:HttpRequest, plant_id:int):
    plant_form = PlantForm()
    plant = Plants.objects.get(pk=plant_id)
    plants = Plants.objects.filter(category=plant.category).exclude(id=plant_id)[:3]

    return render(request,"plants/plant_detail.html",{"plant" : plant, "plants" : plants, "plant_form" : plant_form})

def add_plant_view(request:HttpRequest):
    plant_form = PlantForm()
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('main:home_view')
        else:
            print("not valid form!")
    return render(request,"plants/add_plant.html", {"plant_form":plant_form})

def update_plant_view(request:HttpRequest, plant_id:int):
    plant = Plants.objects.get(pk=plant_id)
    plant_form = PlantForm(instance=plant)

    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES, instance=plant)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('main:home_view')
        else:
            print("not valid form!")
     
    return render(request,"plants/update_plant.html", {"plant" : plant, "plant_form" : plant_form})

def delete_plant_view(request:HttpRequest, plant_id:int):
    plant = Plants.objects.get(pk=plant_id)
    plant.delete()
    return redirect("main:home_view")

def search_plant_view(request:HttpRequest):
    plant_form = PlantForm()
    plants = Plants.objects.all()

    search_query = request.GET.get("search", "")
    category = request.GET.get("category", "")
    is_edible = request.GET.get("is_edible", "")

    if search_query:
        plants = plants.filter(name__icontains=search_query)

    if category:
        plants = plants.filter(category=category)

    if is_edible in ["True", "False"]:
        plants = plants.filter(is_edible=(is_edible == "True"))
    
    return render(request,"plants/search_plant.html", {"plants" : plants, "plant_form" : plant_form})