from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import PlantForm
from .models import Plant





def add_plant_view(request: HttpRequest):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:home_view')
    else:
        form = PlantForm()  # ✅ now 'form' is always defined

    return render(request, "add_plant.html", {'form': form})


def all_plant_view(request:HttpRequest):

    plants = Plant.objects.all()

    return render(request, "all_plants.html", {"plants":plants} )

