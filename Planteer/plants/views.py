from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def plants_all(request:HttpRequest):
  return render(request, "main/plants.html")

def plants_detail(request:HttpRequest):
  return render(request, "main/plants.html")

def plants_new(request:HttpRequest):
  return render(request, "main/plants.html")

def plants_update(request:HttpRequest):
  return render(request, "main/plants.html")

def plants_delete(request:HttpRequest):
  return render(request, "main/plants.html")

def plants_search(request:HttpRequest):
  return render(request, "main/plants.html")
