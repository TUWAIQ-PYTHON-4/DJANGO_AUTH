from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = '__all__'
        exclude = ['user']


class ComForm(forms.Form):
    first_name = forms.CharField(max_length=120)
    content = forms.CharField(widget=forms.widgets.Textarea)
