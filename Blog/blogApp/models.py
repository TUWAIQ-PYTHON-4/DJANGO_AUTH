from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="images")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name
