from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="posts/images")
    def __str__(self):
        return self.title

class Comment(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)

    