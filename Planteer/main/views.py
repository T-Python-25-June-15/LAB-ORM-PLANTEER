from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from . import forms,models

from plants.models import Plant

def home_view(request:HttpRequest):
    plants = Plant.objects.all()

    return render(request,"home.html",
                  {
                      "plants":plants
                  })

def contact_us_view(request:HttpRequest):
    form = forms.ContactForm()
    if request.POST:
        form = forms.ContactForm(request.POST)
        if(form.is_valid()):
            new_message = models.Contact(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],message=request.POST['message'])
            new_message.save()
            return redirect('main:contact_us_messages_view')
            
        

    return render(request, "contactus.html", {"form": form})

def contact_us_messages_view(request:HttpRequest):
    messages = models.Contact.objects.all()

    return render(request, "contactus_messages.html",{
        "messages":messages
    }) 