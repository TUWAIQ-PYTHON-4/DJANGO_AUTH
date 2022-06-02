from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import *

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'index.html', context)

def post(request, post_id):
    form = CommentForm()
    post_info = Post.objects.get(id = post_id)
    post_commints = Comment.objects.filter(post = post_info)

    if request.method == 'POST':
     form = CommentForm(request.POST)
     if form.is_valid():
         commint = Comment.objects.create(post_id = post_id, first_name =  request.POST['first_name']
                                          ,email= request.POST['email'] , content = request.POST['content'])
         return redirect('index')
     else:
         form = CommentForm()

    context = {'post_info': post_info, 'post_commints': post_commints, 'form': form}
    return render(request,'post.html', context)

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







