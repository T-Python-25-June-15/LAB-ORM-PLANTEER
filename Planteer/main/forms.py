from django import forms
from .models import Contact

# Create the form class.
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        '''widgets = {
            'title' : forms.TextInput({"class" : "form-control"})
        }'''