from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact
from .forms import ContactForm

# Create your views here.

def create_form_contact(request: HttpRequest) -> HttpResponse:
    contact_form = Contact()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('contact:show_all_messages')

    return render(request, 'contact/contact_form.html', context={'contact_form':contact_form})


def show_all_messages(request: HttpRequest) -> HttpResponse:
    all_messages = Contact.objects.all()
    return render(request, 'contact/show_all_messages.html', {'all_messages':all_messages})


def delete_message(request: HttpRequest, message_id) -> HttpResponse:
    message = Contact.objects.get(pk=message_id)
    message.delete()
    return redirect('contact:show_all_messages')
