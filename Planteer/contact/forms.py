from django import forms
from contact.models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts 
        fields = "__all__"