from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Plant
from .forms import PlantForm
# Create your views here.


def all_plant_view(request:HttpRequest):
        
    plants = Plant.objects.all()
    
    return render(request, 'plants/all.html', {'plants': plants})

def new_plant_view(request:HttpRequest):
    plant_form = PlantForm()
    if request.method == 'POST':
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('/plants/all/')
        else:
            return redirect('/plants/new/')
    
    return render(request, 'plants/new_plant.html', {'plant_form': plant_form})


def detail_plant_view(request:HttpRequest, plant_id):   
    try:
        plant = Plant.objects.get(pk = plant_id)
        related_plant = Plant.objects.filter(category = plant.category)[:3]#.exclude(pk = [plant.id])
        print(related_plant.count())
        return render(request, 'plants/detail.html', {'plant': plant, 'related_plant': related_plant})
    except Exception as e:
        print(e)
        return redirect('/')
    

def delete_plant(request:HttpRequest, plant_id):
    try:
        Plant.objects.get(pk = plant_id).delete()
        return redirect("/plants/all")
    except Exception as e:
        print(e)
        return redirect('/')
    


def update_plant_view(request:HttpRequest, plant_id):   
    try:
        plant = Plant.objects.get(pk = plant_id)
        
        if request.method == 'POST':
            print('inside post')
            plant_form = PlantForm(request.POST, request.FILES, instance=plant)
            if plant_form.is_valid():
                print('valied')
                plant_form.save()
                return redirect('/plants/{}/detail/'.format(plant.id))
            else:
                print("invailed")
                return redirect('/')
            
        plant_form = PlantForm(instance=plant)
        return render(request, 'plants/update.html', {'plant_form': plant_form, 'plant': plant})
    except Exception as e:
        print(e)
        return redirect('/')