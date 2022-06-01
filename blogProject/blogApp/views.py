from django.shortcuts import render, redirect, resolve_url
from .models import Post, Comment
from .forms import PostModelForm, CommentForm


def index(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            post_list = Post.objects.all()
            context = {"post_list": post_list}
            return render(request, 'index.html', context)
    else:
        post_list = Post.objects.all()
        context = {"post_list": post_list}
        return render(request, 'index.html', context)


def add_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(resolve_url("index"))
    form = PostModelForm()
    context= {'form':form}
    return render(request, 'add-post.html', context)


def post_detail(request):
    return render(request, 'detail.html')
