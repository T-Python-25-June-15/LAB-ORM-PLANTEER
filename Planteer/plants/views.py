from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Plant, Comment
from .forms import PlantForm , CommentForm

# All Page 
def all_view (request:HttpRequest):
    plants = Plant.objects.all()
    return render(request, "plants/all.html", context={"plants" : plants})

# Detail Page
def detail_view (request:HttpRequest, plant_id: int):

    plant = get_object_or_404(Plant,pk = plant_id)

    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.plant = plant
            comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request, "plants/detail.html", context={"plant" : plant, "comment_form" : comment_form, "related_plants" : related_plants})


# Search Page
def search_view (request:HttpRequest):

    query = request.GET.get("search", "")
    order_by = request.GET.get("order_by", "title")
    is_edible = request.GET.get("is_edible")

    plants = Plant.objects.filter(title__icontains=query)

    if is_edible == "true":
        plants = plants.filter(is_edible=True)
    elif is_edible == "false":
        plants = plants.filter(is_edible=False)

    plants = plants.order_by(order_by)

    return render(request, "plants/search.html", context={"plants" : plants, "query" : query})

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
    plant = get_object_or_404(Plant, pk=plant_id)

    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES, instance=plant)
        if plant_form.is_valid():
            plant_form.save()
            return redirect("plants:detail_view", plant_id=plant.id)
        else:
            print("Not valid form")
    else:
        plant_form = PlantForm(instance=plant)
    return render(request, "plants/update.html", context={"plant_form": plant_form, "plant" : plant})
    

# Delete Page
def delete_view (request:HttpRequest, plant_id: int):

    plant = get_object_or_404(Plant, pk=plant_id)

    if request.method == "POST":
        plant.delete()
        return redirect("plants:all_view")
    
    return render(request, "plants/delete_confirm.html", {"plant": plant})



