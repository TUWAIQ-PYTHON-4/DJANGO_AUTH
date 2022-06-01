from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/postsImg")

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}'
