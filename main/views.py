from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import ContactForm
from django.shortcuts import redirect
from .models import Contact

def home_view(request: HttpRequest):
    from plants.models import Plant
    plants = Plant.objects.all().order_by('-created_at')[:6]
    return render(request, "main/home.html", {"plants": plants})

def contact_view(request: HttpRequest):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('main:contact_view')
        else:
            print("not valid form")
    return render(request, "main/contact.html", {"contact_form": contact_form})

def contact_messages_view(request: HttpRequest):
    messages = Contact.objects.all().order_by('-created_at')
    return render(request, "main/contact_messages.html", {"messages": messages})
