from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import PlantForm, CommentForm
from .models import Plant, Comment
from django.core.paginator import Paginator





def add_plant_view(request: HttpRequest):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:home_view')
    else:
        form = PlantForm() 

    return render(request, "add_plant.html", {'form': form})


def all_plant_view(request:HttpRequest):
    
    selected_category = request.GET.get("category")
    plants = Plant.objects.all()

    if selected_category:
        plants = plants.filter(category=selected_category)   
    

    if request.GET.get("is_edible"):
        plants = plants.filter(is_edible = True)

    categories = Plant.CategoryChoices.choices

    paginator = Paginator(plants, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request, "all_plants.html", {"plants": page_obj,"categories": categories, "page_obj":page_obj })


def details_view(request:HttpRequest, plant_id: int):

    plant = Plant.objects.get(pk=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant_id)
    comments = Comment.objects.filter(plant=plant)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.plant = plant
            comment.save()
            return redirect('plant:details_view', plant_id=plant.id)
    else:
        form = CommentForm()

    CATEGORY_COLORS = {
        "Tree": "success",
        "Herb": "info",
        "Flower": "warning",
        "Fruit": "primary",
        "Vegetable": "success",
        "Succulent": "info"
    }

    color_class = CATEGORY_COLORS.get(plant.category, "secondary")
    
    return render(request, "details.html", {
        "plant": plant,
        "color_class": color_class,
        "related_plants": related_plants,
        "form": form,
        "comments": comments
    })



def update_plant_view(request:HttpRequest, plant_id: int):

    plant = Plant.objects.get(pk=plant_id)

    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant:details_view', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant) 

    return render(request, "update_plant.html", {"plant":plant, "form":form, 'plant': plant})


def delete_plant_view(request:HttpRequest, plant_id:int):
    
    plant = Plant.objects.get(pk=plant_id)
    plant.delete()


    return redirect('plant:all_plant_view') 


def search_plant_view(request:HttpRequest):
    
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        plants = Plant.objects.filter(name__contains = request.GET["search"])
    else:
        plants = []  
    
    selected_category = request.GET.get("category")

    if selected_category:
        plants = plants.filter(category=selected_category)
    
    categories = Plant.CategoryChoices.choices
    
    if request.GET.get("is_edible"):
        plants = plants.filter(is_edible = True)


    return render(request,"search_plant.html", {"plants":plants, "categories":categories})


def add_comment_view(request:HttpRequest):

    pass



