from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Home Page
def home_view (request: HttpRequest):
    return render (request, "base.html")


# Contact Page
def contact_view (request: HttpRequest):
    return render(request, "main/contact.html")

# Contact Messages Page
def contact_messages_view(request: HttpRequest):
    return render(request, "main/contact_messages.html")
