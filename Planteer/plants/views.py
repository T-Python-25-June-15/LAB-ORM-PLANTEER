from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
from .forms import PlantForm
from django.contrib import messages
# Create your views here.


def create_plant_view(request:HttpRequest):
    plant_form = PlantForm()

    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            messages.success(request, "Plant updated successfully.")
            return redirect('main:home_view')
        else:
            messages.error(request, "not valid form")

    return render(request, "plants/create_plant.html", {"CategoryChoices": reversed(Plant.CategoryChoices.choices)})



def detail_plant_view(request:HttpRequest, plant_id:int):
    plant = Plant.objects.get(pk = plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3] 

    return render(request, "plants/detail_plant.html", {"plant" : plant, "related_plants" : related_plants})


# def update_plant_view(request:HttpRequest, plant_id:int):
#     plant = Plant.objects.get(pk = plant_id)

#     if request.method =="POST":
#         plant.name = request.POST['name']
#         plant.about = request.POST['about']
#         plant.used_for = request.POST['used_for']
#         plant.category = request.POST['category']
#         plant.is_edible = 'is_edible' in request.POST
#         if "image" in request.FILES: plant.image= request.FILES["image"]
#         plant.save()

#         return redirect("plants:detail_plant_view", plant_id = plant.id)

#     return render(request, "plants/update_plant.html",{"plant" : plant, "CategoryChoices": Plant.CategoryChoices.choices} )


def update_plant_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id)

    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, "Plant updated successfully.")
            return redirect("plants:detail_plant_view", plant_id=plant.id)
        else:
            messages.error(request, "Form is not valid.")
    
    return render(request, "plants/update_plant.html", {"plant": plant, "CategoryChoices": Plant.CategoryChoices.choices})



def delete_plant_view(request:HttpRequest, plant_id:int):
    plant= Plant.objects.get(pk=plant_id)
    plant.delete()

    messages.success(request, "Plant deleted successfully.")
    return redirect('main:home_view')



def all_plant_view(request: HttpRequest):
    plants = Plant.objects.all().order_by('-created_at')

    if "category" in request.GET and request.GET["category"] != "all":
        plants = plants.filter(category=request.GET["category"])

    if "is_edible" in request.GET:
        is_edible_value = request.GET["is_edible"]
        if is_edible_value == "true":
            plants = plants.filter(is_edible=True)
        elif is_edible_value == "false":
            plants = plants.filter(is_edible=False)


    return render(request, 'plants/all_plant.html', {"plants" : plants, "CategoryChoices": Plant.CategoryChoices.choices,})



def search_plants_view(request: HttpRequest):

    if "search" in request.GET and len(request.GET["search"])>=3:
        plants = Plant.objects.filter(name__contains=request.GET["search"])
    else:
        plants = []

    return render(request, 'plants/search_plants.html', {"plants" : plants})

