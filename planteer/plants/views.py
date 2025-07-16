from django.shortcuts import render, redirect, get_object_or_404
from .models import Plant
from .forms import PlantForm 
from django.db.models import Q

# Create your views here.

def plant_list_view(request):
    plants = Plant.objects.all()
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    if category:
        plants = plants.filter(category=category)

    if is_edible == "true":
        plants = plants.filter(is_edible=True)
    elif is_edible == "false":
        plants = plants.filter(is_edible=False)

    context = {
        'plants': plants,
    }
    return render(request, 'plants/plant_list.html', context)

def plant_create_view(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plants:plant_list') 
    else:
        form = PlantForm()

    return render(request, 'plants/plant_form.html', {'form': form})

def plant_search_view(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Plant.objects.filter(
            Q(name__icontains=query) |
            Q(about__icontains=query) |
            Q(used_for__icontains=query) |
            Q(category__icontains=query)
        )

    return render(request, 'plants/plant_search.html', {
        'query': query,
        'results': results
    })

def plant_detail_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    related_plants = Plant.objects.filter(
        category=plant.category
    ).exclude(id=plant.id)[:3] 

    context = {
        'plant': plant,
        'related_plants': related_plants,
    }
    return render(request, 'plants/plant_detail.html', context)

def plant_update_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plants:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)

    return render(request, 'plants/plant_form.html', {'form': form, 'update': True})

def plant_delete_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('plants:plant_list')
    return render(request, 'plants/plant_confirm_delete.html', {'plant': plant})