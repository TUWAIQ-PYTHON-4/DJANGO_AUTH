from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']

class CommentForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    content  = forms.CharField(widget=forms.widgets.Textarea)
    email = forms.EmailField(max_length=50)