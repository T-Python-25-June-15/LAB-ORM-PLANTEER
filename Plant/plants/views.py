from django.shortcuts import render,redirect
from .models import Plant
from .forms import PlantForm
from django.shortcuts import get_object_or_404


# Create your views here.


def plant_list(request):
    plants = Plant.objects.all()

    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    if category and category != 'all':
        plants = plants.filter(category=category)
    
    if is_edible == 'true':
        plants = plants.filter(is_edible=True)
    elif is_edible == 'false':
        plants = plants.filter(is_edible=False)

    context = {
        'plants': plants,
        'selected_category': category or 'all',
        'selected_is_edible': is_edible or 'all',
        'categories': Plant.CATEGORY_CHOICES,
    }
    return render(request, 'plants/plant_list.html', context)

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]
    return render(request, 'plants/plant_detail.html', {'plant': plant, 'related_plants': related_plants})


def plant_create(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plants:plant_list')
    else:
        form = PlantForm()
    return render(request, 'plants/plant_form.html', {'form': form})

def plant_update(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plants:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/plant_form.html', {'form': form, 'update': True})

def plant_delete(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('plants:plant_list')
    return render(request, 'plants/plant_confirm_delete.html', {'plant': plant})


def plant_search(request):
    if 'search' in request.GET:
        query = request.GET['search']
        plants = Plant.objects.filter(name__icontains=query)
    else:
        plants = Plant.objects.none()

    return render(request, 'plants/plant_search.html', {'results': plants})
