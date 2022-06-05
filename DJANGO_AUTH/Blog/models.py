from operator import mod
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    # user
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="movies/images")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
class Comment(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.first_name