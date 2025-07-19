from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
from .forms import PlantForm

# Create your views here.

def all_plants_view(request: HttpRequest):
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')
    plants = Plant.objects.all()
    if category:
        plants = plants.filter(category=category)
    if is_edible in ['true', 'false']:
        plants = plants.filter(is_edible=(is_edible == 'true'))
    plants = plants.order_by("-created_at")

    print(plants.count())

    categories = Plant.Category.choices
    return render(request, "plants/all_plants.html", {
        "plants": plants,
        "categories": categories,
        "selected_category": category,
        "selected_is_edible": is_edible,
    })

def add_plant_view(request: HttpRequest):
    plant_form = PlantForm()
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:all_plants_view')
        else:
            print("not valid form")
    return render(request, "plants/plant_form.html", {"plant_form": plant_form})

def plant_detail_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)[:3]
    return render(request, "plants/plant_detail.html", {"plant": plant, "related_plants": related_plants})


def update_plant_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id)
    plant_form = PlantForm(instance=plant)
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES, instance=plant)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:plant_detail_view', plant_id=plant.id)
    return render(request, "plants/plant_form.html", {"plant_form": plant_form, "plant": plant})


def delete_plant_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id)
    plant.delete()
    return redirect('plants:all_plants_view')

def search_plants_view(request: HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        plants = Plant.objects.filter(name__contains=request.GET["search"])
        if "order_by" in request.GET and request.GET["order_by"] == "category":
            plants = plants.order_by("category")
        elif "order_by" in request.GET and request.GET["order_by"] == "created_at":
            plants = plants.order_by("-created_at")
    else:
        plants = []
    return render(request, "plants/search.html", {"plants": plants})
