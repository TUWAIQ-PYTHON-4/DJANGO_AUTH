from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=240)
    date=models.DateField(auto_now_add=True)
    image= models.ImageField(upload_to="images/")

class comment(models.Model):
    first_name=models.CharField(max_length=50)
    email=models.EmailField()
    content=models.TextField(max_length=240)
    date=models.DateField(auto_now_add=True)