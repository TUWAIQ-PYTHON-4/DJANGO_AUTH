from django.db import models
# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=124)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
