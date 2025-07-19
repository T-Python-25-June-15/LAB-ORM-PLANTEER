from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant,Comment


def all_plants_view(request: HttpRequest):
    plants = Plant.objects.all()
    category = request.GET.get("category")
    is_edible = request.GET.get("is_edible")

    if category and category != "all":
        plants = plants.filter(category=category)

    if is_edible == "true":
        plants = plants.filter(is_edible=True)
    elif is_edible == "false":
        plants = plants.filter(is_edible=False)

    return render(request, "plant/all_plants.html", {"plants": plants,"CategoryChoices": Plant.CategoryChoices.choices})


def plant_detail_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id)
    related_plants = Plant.objects.filter(category=plant.category)[0:3]
    comments= Comment.objects.filter(plant=plant)

    
    return render(request, 'plant/plant_detail.html', {'plant': plant, 'related_plants': related_plants , 'comments':comments})


def add_plant_view(request: HttpRequest):
    if request.method == "POST":
        new_plant = Plant(
            name=request.POST["name"],
            about=request.POST["about"],
            used_for=request.POST["used_for"],
            category=request.POST["category"],
            is_edible=True if request.POST.get("is_edible") == "on" else False,
            image=request.FILES.get("image")
        )
        new_plant.save()
        return redirect('plant:all_plants_view')

    return render(request, 'plant/add_plant.html', {"CategoryChoices": Plant.CategoryChoices.choices})


def plant_update_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id) 

    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        plant.category = request.POST["category"]
        plant.is_edible = True if request.POST.get("is_edible") == "on" else False

        if "image" in request.FILES:
            plant.image = request.FILES["image"]

        plant.save()
        return redirect('plant:plant_detail_view', plant_id=plant.id)

    return render(request, 'plant/plant_update.html', {'plant': plant, "CategoryChoices": Plant.CategoryChoices.choices})

def plant_delete_view(request:HttpRequest,plant_id:int):

    plant=Plant.objects.get(pk=plant_id)
    plant.delete()

    return redirect("plant:all_plants_view")

def search_plant_view(request: HttpRequest):
    search_input = request.GET.get("search")
    
    if search_input:
        plants = Plant.objects.filter(name__icontains=search_input)
    else:
        plants = Plant.objects.none()
    
    return render(request, 'plant/search_plant.html', {'plants': plants, 'search_input': search_input})


def add_comment_view(request: HttpRequest, plant_id):
    if request.method == "POST":
        plant_object = Plant.objects.get(pk=plant_id)
        new_comment = Comment(
            plant=plant_object,
            name=request.POST["name"],
            comment=request.POST["comment"]
        )
        new_comment.save()

    return redirect("plant:plant_detail_view", plant_id=plant_id)

