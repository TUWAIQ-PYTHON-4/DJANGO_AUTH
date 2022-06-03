from .models import comment,Post
from django.forms import ModelForm

class Postform(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class Commentform(ModelForm):
    class Meta:
        model = comment
        fields = ('first_name', 'content')