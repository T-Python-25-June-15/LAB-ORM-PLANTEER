from django.shortcuts import get_object_or_404, render, redirect
from plants.models import Plant
from .forms import ContactForm
from .models import Contact

# Create your views here.

def home_view(request):
    #to retrieve plant informations (attributes)
    #stored into featured_plants
    featured_plants = Plant.objects.all()[:3]
    return render(request, 'main/home.html', {'featured_plants': featured_plants})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def contact_messages_view(request):
    messages = Contact.objects.order_by('-created_at')
    return render(request, 'main/contact_messages.html', {'messages': messages})

def delete_contact_message(request, pk):
    contact_msg = get_object_or_404(Contact, pk=pk)
    contact_msg.delete()
    return redirect('main:contact_messages')