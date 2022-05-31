from django import forms
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']


class CommentForm(forms.Form):
    name = forms.CharField(max_length=124)
    content = forms.CharField(widget=forms.widgets.Textarea)
