from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
