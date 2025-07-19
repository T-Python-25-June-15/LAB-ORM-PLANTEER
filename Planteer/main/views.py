from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plants
from .models import Contact
from .forms import ContactForm
# Create your views here.

def home_views(request:HttpRequest):
    plants = Plants.objects.all().order_by("-created_at")[0:3]
    return render(request, 'main/home.html', {"plants":plants} )


def contact_us_views(request:HttpRequest):
    contect_form = ContactForm()
    sumbitted = False
    if request.method == "POST":
        contect_form = ContactForm(request.POST, request.FILES)
        if contect_form.is_valid():
            contect_form.save()
            sumbitted = True
        else:
            print('not valid form')
    return render(request, 'main/contact.html',{"contect_form":contect_form, "sumbitted":sumbitted})


def messages_views(request:HttpRequest):
    messages = Contact.objects.all().order_by("-created_at")
    return render(request, 'main/contact__us_message.html', {"messages":messages} )
