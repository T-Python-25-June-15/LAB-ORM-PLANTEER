from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plants,Comment

def plants_all(request:HttpRequest):
  plant = Plants.objects.all()
  return render(request, "plants/plants_all.html", {"plant":plant})

def plants_detail(request:HttpRequest, plant_id:int):
  plants = Plants.objects.all()
  plant = Plants.objects.get(pk=plant_id)
  comments = plant.comments.all()

  if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        if name and text:
            Comment.objects.create(plant=plant, name=name, text=text)
            return redirect('plants:plants_detail', plant_id=plant_id)
        
  return render(request, "plants/detail.html", {"plants":plants,"plant_info":plant,"comments":comments})

def plants_new(request:HttpRequest):
  if request.method == "POST":

    status = False
    if request.POST["is_editable"] == 1:
      status = True

    plant = Plants(name=request.POST["name"],about=request.POST["about"],used_for=request.POST["used_for"],category=request.POST["category"],is_editable = status, created_at = request.POST["created_at"], image = request.FILES["image"])
    print("posted")
    plant.save()
    

  return render(request, "plants/new.html")

def plants_edit(request: HttpRequest, plant_id: int):
  plant = Plants.objects.get(pk=plant_id)

  if request.method == "POST":
      plant.name = request.POST["name"]
      plant.about = request.POST["about"]
      plant.used_for = request.POST["used_for"]
      plant.category = request.POST["category"]
      plant.is_editable = request.POST["is_editable"] == "1"
      plant.created_at = request.POST["created_at"]

      if "image" in request.FILES:
        plant.image = request.FILES["image"]

      plant.save()
  return render(request, "plants/edit.html", {"plant": plant})

def plants_update(request:HttpRequest):
  return render(request, "plants/plants.html")

def plants_delete(request:HttpRequest, plant_id: int):
  plant = Plants.objects.get(pk=plant_id)
  plant.delete()
  return redirect("main:main_page")

def plants_search(request: HttpRequest):
    query = request.GET.get('search', '')
    result = []
    if query:
        result = Plants.objects.filter(name__icontains=query)
    return render(request, "plants/search.html", {"result": result, "search": query})
