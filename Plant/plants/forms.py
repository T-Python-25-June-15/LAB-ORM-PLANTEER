from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'description', 'image', 'category', 'is_edible', 'native_to', 'used_for']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'is_edible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'native_to': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Saudi Arabia, USA'}),
            'used_for': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'e.g. Salads, Medicine'}),
        }
