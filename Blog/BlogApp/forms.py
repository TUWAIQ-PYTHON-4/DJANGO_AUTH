from django import forms
from .models import Post ,Comments


class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"

