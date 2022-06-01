from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import *

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'index.html', context)

def post(request, post_id):
    post_info = Post.objects.get(id = post_id)
    post_commints = Comment.objects.filter(post = post_info)
    context = {'post_info': post_info, 'post_commints': post_commints}
    return render(request,'post.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html',context )

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(user_id=request.user.id, title=request.POST['title']
                    , content = request.POST['content'],image = request.FILES['image'])
            return redirect('index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post_form.html',context )





