from django import forms
from plants.models import Plants

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plants 
        fields = "__all__"