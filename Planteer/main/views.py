from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from plant.models import Plant
from main.models import Contact
from main.forms import ContactForm


def home_view(request: HttpRequest):
    plants = Plant.objects.order_by('-created_at')[0:3]
    return render(request, 'main/home.html', {"plants": plants})

def contact_view(request: HttpRequest):
    success_message = None
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Your message has been sent successfully. Thank you."
            form = ContactForm() 

    return render(request, 'main/contact.html', {'form': form, 'success_message': success_message})


def messages_view(request:HttpRequest):
    messages = Contact.objects.all()

    return render(request, 'main/messages.html', {'messages': messages})