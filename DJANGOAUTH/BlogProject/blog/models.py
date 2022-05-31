from django.contrib.auth.models import User
from django.db import models


class Post (models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='posts/photos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Comment(models.Model):
    first_name = models.CharField(max_length=124)
    email = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)