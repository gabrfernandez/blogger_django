from .models import *
from django import forms

class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'class':'single-input','placeholder':'Title'}),
            'content' : forms.Textarea(attrs={'class':'single-input', 'placeholder':'Content'})
        }

        fields = ['title', 'category', 'content', 'image', ]