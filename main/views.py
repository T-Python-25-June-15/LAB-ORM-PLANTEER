from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Plants , Review  
from django.utils import timezone



def home_view(request : HttpRequest) :
    plants = Plants.objects.all().order_by('created_at')[0:3]
    return render(request, "main/home.html", {'plants': plants})


def add_plant(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        about = request.POST.get('about')
        used_for = request.POST.get('used_for')
        category = request.POST.get('category')
        is_edible = request.POST.get('is_edible') == 'on'
        image = request.FILES.get('image')

        plant = Plants(
            name=name,
            about=about,
            used_for=used_for,
            category=category,
            is_edible=is_edible,
            image=image if image else 'images/default.png',
            created_at=timezone.now()
        )
        plant.save()

        return redirect('main:home_view')

    return render(request, 'main/add_plant.html')

def plant_detail_view(request:HttpRequest, plant_id:int):

    plant = Plants.objects.get(pk=plant_id)
    reviews = Review.objects.filter(plant=plant)
    related_plants = Plants.objects.filter(category=plant.category).exclude(id=plant.id)[:4]


    return render(request, 'main/plant_detail.html', {"plant" : plant,'reviews':reviews ,'related_plants': related_plants})

def plant_update_view(request: HttpRequest, plant_id):
    plant = get_object_or_404(Plants, id=plant_id)

    if request.method == 'POST':
        plant.name = request.POST.get('name')
        plant.about = request.POST.get('about')
        plant.used_for = request.POST.get('used_for')
        plant.category = request.POST.get('category')
        plant.is_edible = request.POST.get('is_edible') == 'on'

        image = request.FILES.get('image')
        if image:
            plant.image = image

        plant.save()
        return redirect('main:home_view')

    return render(request, 'main/update_plant.html', {'plant': plant})

def plant_delete_view(request:HttpRequest, plant_id:int):

    plant = Plants.objects.get(pk=plant_id)
    plant.delete()

    return redirect("main:home_view")

def all_plant_view(request: HttpRequest):
    plants = Plants.objects.all().order_by("created_at")

    category = request.GET.get("category")
    if category:
        plants = plants.filter(category=category)

    is_edible = request.GET.get("is_edible")
    if is_edible == "true":
        plants = plants.filter(is_edible=True)
    elif is_edible == "false":
        plants = plants.filter(is_edible=False)

    categories = Plants.objects.values_list("category", flat=True).distinct()

    return render(request, "main/all_plant.html", {"plants": plants,"categories": categories})


def search_plants_view(request:HttpRequest):
    search_query = request.GET.get("search", "").strip()
    plants = []

    if len(search_query) >= 3:
        plants = Plants.objects.filter(name__icontains=search_query)

    return render(request, "main/search_plants.html", {"plants": plants, "search": search_query})


def add_review_view(request:HttpRequest , plant_id):
   if request.method == "POST":
      plant_object = Plants.objects.get(pk=plant_id)
      new_review = Review(plant=plant_object , name=request.POST["name"], comment =request.POST["comment"])
      new_review.save()
    
   return redirect("main:plant_detail_view" , plant_id=plant_id)