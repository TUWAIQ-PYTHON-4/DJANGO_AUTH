from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#Post (user , title, content, date , image) . Note : for user make sure to use the User model from Django
#Comment (first_name, email, content, date)
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    post_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return '/detail/{}'.format(self.pk)
    class Meta:
        ordering=('-post_date', )

class Comment(models.Model):
    first_name=models.CharField(max_length=50)
    email=models.EmailField()
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    active=models.BooleanField(default=False)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.first_name






