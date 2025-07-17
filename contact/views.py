from django.shortcuts import render,  redirect

from .models import Contact
from .forms import ContactForm
# Create your views here.



def contact_view(request):
    
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/messages/')
    return render(request, 'contact/contact.html', {'form':form})

def all_contact(request):
    
    contacts = Contact.objects.all()
    
    return render(request, 'contact/all.html', {'contacts': contacts})