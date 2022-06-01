from django import forms
from .models import Post, Comment


class addForm(forms.Form):
    class Meta:
        model = Post
        fields = '__all__'



class addComment(forms.Form):
    class Meta:
        model = Comment
        fields = '__all__'
