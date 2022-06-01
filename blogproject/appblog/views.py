from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import *


def index(request):
    all_posts = Post.objects.all()
    context_post = {"all_post": all_posts}
    return render(request, 'index.html', context_post)





