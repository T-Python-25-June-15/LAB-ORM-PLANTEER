from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Plants

def plants_all(request:HttpRequest):
  return render(request, "plants/plants_all.html")

def plants_detail(request:HttpRequest, plant_id):
  plant = Plants.objects.get(pk=plant_id)
  print(plant)

  return render(request, "plants/detail.html")

def plants_new(request:HttpRequest):
    #   name = models.CharField(default="Plant")
    # about = models.TextField(default="Soon!")
    # used_for = models.TextField(default="Soon!")
    # image = models.ImageField(default="images/default.jpg")
    # category = models.CharField(default='Fruit')
    # is_editable = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)

  plant = Plants(name="Kmthrh",about="nothing is here",used_for="eating cooking",category = "fruit",is_editable = True)
  return render(request, "plants/plants.html")

def plants_update(request:HttpRequest):
  return render(request, "plants/plants.html")

def plants_delete(request:HttpRequest):
  return render(request, "plants/plants.html")

def plants_search(request:HttpRequest):
  return render(request, "plants/plants.html")
