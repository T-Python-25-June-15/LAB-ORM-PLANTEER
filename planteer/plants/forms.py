from django import forms
from .models import Plant, Comment

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }