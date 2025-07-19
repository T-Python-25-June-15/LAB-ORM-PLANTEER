from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant, Comment
from .forms import PlantForm, CommentForm

# Home page view - shows the latest 3 added plants
def home_view(request):
    latest_plants = Plant.objects.order_by('-created_at')[:3]
    return render(request, 'plants/home.html', {'latest_plants': latest_plants})

# View for listing all plants with optional filtering by category and edibility
def all_plants(request):
    plants = Plant.objects.all()
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    if category:
        plants = plants.filter(category=category)
    if is_edible:
        if is_edible.lower() == 'true':
            plants = plants.filter(is_edible=True)
        elif is_edible.lower() == 'false':
            plants = plants.filter(is_edible=False)

    return render(request, 'plants/all.html', {'plants': plants})

# Plant detail view - shows details, related plants, comments, and allows adding new comments
def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]
    comments = plant.comments.order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.plant = plant
            comment.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        comment_form = CommentForm()

    context = {
        'plant': plant,
        'related_plants': related_plants,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'plants/detail.html', context)

# Add a new plant
def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()
    return render(request, 'plants/form.html', {'form': form, 'title': 'Add Plant'})

# Update an existing plant
def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/form.html', {'form': form, 'title': 'Update Plant'})

# Delete a plant
def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('all_plants')
    return render(request, 'plants/delete.html', {'plant': plant})

# Search for plants by name
def search_plants(request):
    query = request.GET.get('q')
    results = Plant.objects.filter(name__icontains=query) if query else []
    return render(request, 'plants/search.html', {'results': results, 'query': query})

# Add a comment manually without using the ModelForm
def add_comment(request, plant_id):
    if request.method == "POST":
        plant_object= Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant= plant_object, plantname= request.POST['full_name'],content=request.POST["content"])
        new_comment.save()
    return redirect('plant_detail', plant_id=plant_id)

