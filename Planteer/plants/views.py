from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import PlantForm
from .models import Plants
# Create your views here.

def add_views(request:HttpRequest):
    plant_form = PlantForm()
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('main:home_views')
        else:
            print('not valid form')
    return render(request, "plants/add.html", {"plant_form":plant_form,"CategoryChoices": reversed(Plants.CategoryChoices.choices)})

def all_views(request:HttpRequest):
    plants = Plants.objects.all().order_by("-created_at")
    return render(request, 'plants/all_plants.html', {"plants":plants} )


def details_views(request:HttpRequest, plant_id:int):
    plant = Plants.objects.get(pk=plant_id)
    return render(request, "plants/details.html", {"plants":plant})


def update_views(request:HttpRequest, plant_id:int):
    plant = Plants.objects.get(pk=plant_id)
    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.user_for = request.POST["user_for"]
        if "image" in request.FILES: plant.image = request.FILES["image"]
        plant.category = request.POST["category"]
        plant.is_edible = request.POST["is_edible"]
        plant.created_at = request.POST["created_at"]
        plant.save()

        return redirect("plants:details_views", plant_id=plant.id)
    return render(request, "plants/update.html", {"plants":plant})
    
def delete_views(request:HttpRequest, plant_id:int):
    plant = Plants.objects.get(pk=plant_id)
    plant.delete()
    return redirect("main:home_views")

def search_views(request:HttpRequest):
    plants = Plants.objects.all()
    search_result = request.GET.get("search","")
    category_filter = request.GET.get("category","")
    is_edible_filter = request.GET.get("is_edible","")

    if len(search_result) >= 3:
        plants = plants.filter(name__contains=search_result)

    if category_filter:
            plants = plants.filter(category=category_filter)
    if is_edible_filter:
            plants = plants.filter(is_edible=(is_edible_filter == "True"))

    return render(request, "plants/search.html", {"plants" : plants})