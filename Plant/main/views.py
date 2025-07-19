from django.shortcuts import render,redirect
from plants.models import Plant
from .forms import ContactForm
from .models import Contact

def home(request):
    featured_plants = Plant.objects.all()[:3]
    return render(request, 'main/home.html', {'plants': featured_plants})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('main:contact_success')  
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def contact_messages_view(request):
    messages = Contact.objects.all().order_by('-created_at') 
    context = {
        'messages': messages,
    }
    return render(request, 'main/contact_messages.html', context)

def contact_success_view(request):
    return render(request, 'main/contact_success.html')