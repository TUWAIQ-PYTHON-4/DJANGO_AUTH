from django.db import models

# Create your models here.
# You have 2 Models:
# Post (user , title, content, date , image)
# . Note : for user make sure to use the User model from Django
# Comment (first_name, email, content, date)
from django.db import models


class Post(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/images/')

    def __str__(self):
        return self.title


class Comments(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.email + self.content + str(self.date) + str(self.post)
