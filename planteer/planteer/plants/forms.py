from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'about', 'used_for', 'image', 'category', 'is_edible']
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'used_for': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }