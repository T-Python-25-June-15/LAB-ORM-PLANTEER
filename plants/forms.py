from django import forms
from .models import Plant, Comment


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'about': forms.Textarea(attrs={"class": "form-control"}),
            'used_for': forms.Textarea(attrs={"class": "form-control"}),
            'image': forms.ClearableFileInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-select"}),
            'is_edible': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.Textarea(attrs={"class": "form-control"}),
        } 