from django.shortcuts import render
from .models import Post


# Create your views here.

def Blog(request):
    blog = Post.objects.all()
    return render(request, 'index.html', {'blog': blog})


def ShowDetials(request, id):
    blog = Post.objects.get(id=id)
    return render(request, 'detalis.html', {'blog': blog})


def Comment(request,id):
    comment = Comment.objects.get(id=id)
    return render(request, 'deatils.html', {'comment': comment})
