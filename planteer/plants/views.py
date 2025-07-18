from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Plant
from .forms import PlantForm

# ---------- Home ----------
def home(request):
    plants = Plant.objects.all()[:3]
    return render(request, 'main/home.html', {'plants': plants})

# ---------- All Plants ----------
def all_plants(request):
    category_filter = request.GET.get('category')
    is_edible_filter = request.GET.get('is_edible')

    plants = Plant.objects.all()

    if category_filter:
        plants = plants.filter(category=category_filter)
    
    if is_edible_filter in ['True', 'False']:
        plants = plants.filter(is_edible=(is_edible_filter == 'True'))

    return render(request, 'plants/all_plants.html', {'plants': plants})

# ---------- Plant Detail ----------
def plant_detail(request, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
    except Plant.DoesNotExist:
        raise Http404("Plant not found")

    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)
    return render(request, 'plants/plant_detail.html', {
        'plant': plant,
        'related_plants': related_plants
    })

# ---------- Add Plant ----------
def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plant')
    else:
        form = PlantForm()
    
    return render(request, 'plants/add_plant.html', {'form': form})

# ---------- Update Plant ----------
def update_plant(request, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
    except Plant.DoesNotExist:
        raise Http404("Plant not found")

    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)

    return render(request, 'plants/update_plant.html', {
        'form': form,
        'plant': plant
    })

# ---------- Delete Plant ----------
def delete_plant(request, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
    except Plant.DoesNotExist:
        raise Http404("Plant not found")

    if request.method == 'POST':
        plant.delete()
        return redirect('all_plant')

    return redirect('all_plant')



# ---------- Search ----------

def search_plant(request):
    try:
        query = request.GET.get('q', '')
        if query:
            results = Plant.objects.filter(name__icontains=query) 
        else:
            results = Plant.objects.all()  
    except Exception as e:
        print(f"Error occurred while searching for plants: {e}")

    return render(request, 'plants/search.html', {
        'results': results
    })

