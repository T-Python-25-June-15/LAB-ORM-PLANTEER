from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
from .forms import PlantForm

# All Page 
def all_view (request:HttpRequest):
    plants = Plant.objects.all()
    return render(request, "plants/all.html", context={"plants" : plants})

# Detail Page
def detail_view (request:HttpRequest, plant_id: int):
    return render(request, "plants/detail.html")

# Search Page
def search_view (request:HttpRequest):
    return render(request, "plants/search.html")

# New Page
def new_view (request:HttpRequest):
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect("plants:all_view")
        else:
            print("not valid form")
    else:
        plant_form = PlantForm()
    return render(request, "plants/new.html", {"plant_form" : plant_form})

# Update Page
def update_view (request:HttpRequest, plant_id: int):
    return render(request, "plants/update.html")

# Delete Page
def delete_view (request:HttpRequest, plant_id: int):
    return render(request, "plants/delete.html")


