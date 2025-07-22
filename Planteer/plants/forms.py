from django import forms
from plants.models import Plant,Comment

# Create the form class.
class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"