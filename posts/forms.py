from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field,Submit

class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'class':'single-input','placeholder':'Title'}),
            'content' : forms.Textarea(attrs={'class':'single-input', 'placeholder':'Content'})
        }

        fields = ['title', 'category', 'content', 'image', ]

class PostUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method='POST'
        self.helper.field_class = 'mt-10'
        self.helper.layout = Layout(
            Field("title", css_class="single-input", placeholder="Title"),
            Field("category", css_class="single-input"),
            Field("content", css_class="single-input", placeholder="Content"),
            Field("image", css_class="single-input"),
            Field("tag", css_class="single-input", placeholder="Tag", value=self.instance.post_tag()),
        )
        self.helper.add_input(Submit('submit', 'Update', css_class='genric-btn success circle'))

    tag = forms.CharField()
    class Meta:
        model = Post
        fields = [ 'title', 'category', 'content', 'image']
