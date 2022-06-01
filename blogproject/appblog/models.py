from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.user


class Comment(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
