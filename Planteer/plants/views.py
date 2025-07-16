from django.shortcuts import render,redirect
from django.http import HttpRequest
from . import forms
from .models import Plant, Comment

def all_plants_view(request:HttpRequest):
    plants = Plant.objects.all()
    return render(request,'all.html', {
        "plants" : plants
    })


def add_plant_view(request: HttpRequest):
    if request.method == "POST":
        plant_form = forms.plantsForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:all_plants_view')
    else:
        plant_form = forms.plantsForm()

    return render(request, "add.html", {
        "form": plant_form
    })


def plant_details_view(request:HttpRequest,plant_id):
    plant = Plant.objects.get(pk=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)
    plant_comments = plant.comments.all()
    return render(request,"plant_detail.html", {
        "plant":plant,
        'related_plants':related_plants,
        "plant_comments":plant_comments
    })

def update_plant_view(request:HttpRequest, plant_id:int):
    plant = Plant.objects.get(pk=plant_id)
    plant_form = forms.plantsForm(instance=plant)
    if request.method == "POST":
        plant_form = forms.plantsForm(request.POST, request.FILES, instance=plant)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:all_plants_view')
        else:
            plant_form = forms.plantsForm(instance=plant)

 



    return render(request,'update_plant.html',{
        "plant":plant,
        "plant_form":plant_form
    })


def delete_plant_view(request:HttpRequest, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    if plant:
        plant.delete()
        return redirect('plants:all_plants_view')


def search_plants_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 3:
        plants = Plant.objects.filter(name__contains=request.GET["search"])

        if "order_by" in request.GET and request.GET["order_by"] == "name":
            plants = plants.order_by("name")
        elif "order_by" in request.GET and request.GET["order_by"] == "category":
            plants = plants.order_by("-category")
        elif "order_by" in request.GET and request.GET["order_by"] == "created_at":
            plants = plants.order_by("-created_at")
    else:
        plants = []


    return render(request, "search.html", {"plants" : plants})


def add_plant_comment_view(request:HttpRequest, plant_id):
    if request.POST:
        plant_obj = Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant =plant_obj, full_name=request.POST['full_name'],content=request.POST['content'])
        new_comment.save()
        return redirect('plants:plant_details_view',plant_id= plant_id)