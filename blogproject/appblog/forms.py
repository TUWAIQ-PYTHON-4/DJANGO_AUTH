from .models import *
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
