from django import forms
from .models import Post, Comment
from django.forms import ModelForm


class push_post(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
