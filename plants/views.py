from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

        return redirect('plants:contact_messages_view')

    return render(request, 'contact/contact_view.html')

def contact_messages_view(request):
    messages_list = Contact.objects.order_by('-created_at') 
    return render(request, 'contact/contact_messages.html', {'messages': messages_list})

def contact_message_delete(request, pk):
    message = get_object_or_404(Contact, pk=pk)
    message.delete()
    return redirect('plants:contact_messages_view')