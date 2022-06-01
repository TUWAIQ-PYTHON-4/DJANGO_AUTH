from django import forms
from .models import Comment, Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.Form):
    first_name=forms.CharField(max_length=50)
    content = forms.CharField(max_length=250)

