from django import forms
from .models import Plants

# Create the form class.
class PlantForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = "__all__"
        '''widgets = {
            'title' : forms.TextInput({"class" : "form-control"})
        }'''