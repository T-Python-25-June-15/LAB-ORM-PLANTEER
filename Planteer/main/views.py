from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plant
from django.db.models import Q
from .forms import ContactForm
from django.contrib import messages
from .models import Contact

# Create your views here.
def home_view(request : HttpRequest):
    # content = "hello from home page"
    # return HttpResponse(content)
    recent_plants = Plant.objects.prefetch_related('reviews').order_by('-created_at')[:3]
    return render(request, "main/home.html", {"recent_plants": recent_plants})



def search_view(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Plant.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))

    return render(request, 'main/search.html', {'results': results})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message submitted successfully")
            return redirect('main:contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def messages_view(request):
    contacts = Contact.objects.order_by('-created_at')
    return render(request, 'main/messages.html', {'contacts': contacts})