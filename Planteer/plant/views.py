from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant, Comment
from .forms import PlantForm
from datetime import datetime

# Create your views here.

def newPlant_view(request:HttpRequest):
     plant_form = PlantForm()
     if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('main:home_view')
        else:
            print(plant_form.errors)
            print("not valid form")
     return render(request, "plant/AddPlant.html",{"plant_form":plant_form , "CategoryChoices": Plant.CategoryChoices.choices})


def AllPlant_view(request:HttpRequest):
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    plants = Plant.objects.all()

    if category and category != 'all':
        plants = plants.filter(category=category)

    if is_edible == 'true':
        plants = plants.filter(is_edible=True)
    elif is_edible == 'false':
        plants = plants.filter(is_edible=False)

    return render(request, "plant/AllPlants.html", {
        "plant": plants,
        "CategoryChoices": Plant.CategoryChoices.choices,
        "selected_category": category,
        "is_edible": is_edible,
    })

def detail_view(request:HttpRequest, plant_id:int):
      plant = Plant.objects.get(pk=plant_id)
      same_category = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[0:3]
      comments = Comment.objects.filter(plant=plant)
      return render(request, 'plant/detail.html', {
        "plant": plant,
        "same_category": same_category,
        "comment" : comments, 
})

def update_view(request:HttpRequest, plant_id:int):
    plant = Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        if "image" in request.FILES: plant.image = request.FILES["image"]
        plant.category = request.POST["category"]
        plant.is_edible = request.POST["is_edible"]  
        plant.save()
        return redirect("plant:detail_view", plant_id)

    return render(request, "plant/UpdatePlant.html", {"plant":plant, "CategoryChoices": Plant.CategoryChoices.choices})


def delete_view(request:HttpRequest, plant_id:int):
     plant= Plant.objects.get(pk=plant_id)
     plant.delete()
     return redirect('main:home_view')

def search_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 3:

        plant = Plant.objects.filter(name__contains=request.GET["search"])
    else:
        plant = []

    return render(request, "plant/search.html", {"plant" : plant})

def add_comment_view(request:HttpRequest, plant_id):
    if request.method == "POST": 
        plant = Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant= plant , full_name= request.POST["full_name"], plant_relation= request.POST["plant_relation"], 
                            content= request.POST["content"])
        new_comment.save()
    

    return redirect("plant:detail_view", plant_id= plant_id )

