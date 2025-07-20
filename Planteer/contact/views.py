
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
# Create your views here.



def contact_form_view(request:HttpRequest):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect("contact:contact_messages_view")
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, "contact/contact_form.html")





def contact_messages_view(request:HttpRequest):
    user_messages = Contact.objects.all().order_by('created_at')

    return render(request, "contact/contact_massages.html", {"user_messages": user_messages})


