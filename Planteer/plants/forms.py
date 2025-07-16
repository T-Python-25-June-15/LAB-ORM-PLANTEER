from django import forms

from . import models

class plantsForm(forms.ModelForm):
    class Meta:
        model = models.Plant
        fields = "__all__"
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'border border-gray-400 p-2 w-full py-1 h-10 rounded-lg mt-1',
            'placeholder': 'plant name',
            'required': 'required',
        })
    )
    about = forms.CharField(
        widget=forms.Textarea(attrs={
        'class': 'border border-gray-400 p-2 w-full py-1 h-24 rounded-lg mt-1',
        'placeholder': 'about plant',
        'required': 'required',
    })
)
    used_for = forms.CharField(
        widget=forms.Textarea(attrs={
        'class': 'border border-gray-400 p-2 w-full py-1 h-24 rounded-lg mt-1',
        'placeholder': 'plant used for',
        'required': 'required',
    })
)
    category = forms.ChoiceField(
        choices=models.Plant.CategoriesChoices.choices,
        widget=forms.Select(attrs={
            'class': 'border border-gray-400 p-2 w-full py-1 h-10 rounded-lg mt-1',
            'required': 'required',
        }),
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'border border-gray-400 p-2 w-full py-1 h-10 rounded-lg mt-1',
        }),
    )    
    is_edible = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'mr-2 h-5 w-5 text-blue-600 border-gray-300 rounded m-5 reverse',
        })
    )  
