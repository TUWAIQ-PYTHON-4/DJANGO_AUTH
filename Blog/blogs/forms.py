
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.Form):

     name = forms.CharField(max_length=150)
     content = forms.CharField(widget=forms.widgets.Textarea)

