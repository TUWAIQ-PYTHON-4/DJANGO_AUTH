from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add= True)
    image=models.ImageField(upload_to='imeges/')

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    first_name=models.CharField(max_length=50)
    email=models.EmailField()
    date=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'comments')

    def __str__(self) -> str:
        return self.first_name