from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest,HttpResponse
from .forms import PlantForm
from .models import Plant,Review
# Create your views here.


def add_plant(request: HttpRequest):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plants:all_plants')
    else:
        form = PlantForm()
    
    return render(request, 'plants/add.html', {'form': form})


def all_plants_view(request):
    category_filter = request.GET.get('category')
    is_edible_filter = request.GET.get('is_edible')

    plants = Plant.objects.order_by('-created_at')

    if category_filter and category_filter != 'All':
        plants = plants.filter(category=category_filter)

    if is_edible_filter == 'true':
        plants = plants.filter(is_edible=True)
    elif is_edible_filter == 'false':
        plants = plants.filter(is_edible=False)

    categories = Plant.PlantCategory.choices

    return render(request, 'plants/all.html', {
        'plants': plants,
        'categories': categories,
        'current_category': category_filter,
        'current_edible': is_edible_filter
    })
    
def plant_detail_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]
    reviews = plant.reviews.all().order_by('-created_at')
    return render(request, 'plants/detail.html', {'plant': plant, 'related_plants': related_plants, 'reviews': reviews })


def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plants:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/update.html', {'form': form, 'plant': plant})

def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('plants:all_plants')  
    return render(request, 'plants/delete.html', {'plant': plant})

def add_review(request: HttpRequest, plant_id):
    if request.method == "POST":
        plant = get_object_or_404(Plant, pk=plant_id)
        Review.objects.create(
            plant=plant,
            name=request.POST["name"],
            rating=request.POST["rating"],
            comment=request.POST["comment"]
        )
    return redirect("plants:plant_detail", plant_id=plant.id)

