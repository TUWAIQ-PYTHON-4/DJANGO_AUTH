from django import forms


from django import forms
from .models import Post , Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = '__all__'

