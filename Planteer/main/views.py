from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from plants.models import Plants

def main_page(request: HttpRequest):
  plant = Plants.objects.all()
  return render(request, "main/index.html", {"plant":plant})
