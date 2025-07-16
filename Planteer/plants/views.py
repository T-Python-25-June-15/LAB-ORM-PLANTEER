from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# All Page 
def all_view (request:HttpRequest):
    return render(request, "plants/all.html")

# Detail Page
def detail_view (request:HttpRequest, plant_id: int):
    return render(request, "plants/detail.html")

# Search Page
def search_view (request:HttpRequest):
    return render(request, "plants/search.html")

# New Page
def new_view (request:HttpRequest):
    return render(request, "plants/new.html")

# Update Page
def update_view (request:HttpRequest, plant_id: int):
    return render(request, "plants/update.html")

# Delete Page
def delete_view (request:HttpRequest, plant_id: int):
    return render(request, "plants/delete.html")


