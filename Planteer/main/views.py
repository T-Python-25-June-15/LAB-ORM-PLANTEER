from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plant.models import Plant
from main.models import Contact
# Create your views here.

def home_view(request:HttpRequest):
    plants = Plant.objects.all().order_by('-created_at')[0:3]
    return render(request, 'main/home.html', {"plant":plants} )

def contact_view(request:HttpRequest):
     
     if request.method == "POST":
        message = Contact(first_name=request.POST["first_name"], last_name=request.POST["last_name"], 
                         email=request.POST["email"], 
                         message = request.POST["message"])
               
        message.save()
        return redirect('main:home_view')

     return render(request,"main/contact.html")

def messages_view(request:HttpRequest):
    message = Contact.objects.all()
    return render(request,"main/messages.html",{"message": message})
