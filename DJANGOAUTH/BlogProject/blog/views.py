from django.http import HttpRequest
from django.shortcuts import render, redirect, resolve_url
from .forms import PostModelForm
from BlogProject.blog.models import Post


def index(request : HttpRequest):

    post = Post.objects.all()

    context = {"posts": post, "display": True}

    if request.user.is_authenticated:
        context["user"] = request.user
        print("is authenticated")
    else:
        return redirect(resolve_url("accounts:login"))





def add_movie(request : HttpRequest):


    if not request.user.has_perm("blog.add_blog"):
        return redirect(resolve_url("accounts:login"))

    if request.method == 'POST':
        postModelForm = PostModelForm(request.POST, request.FILES)

        if movieModelForm.is_valid():
            #add model
            blog = Post(user=request.user,  **postModelForm.cleaned_data)
            blog.save()
            return redirect(resolve_url("blog:index"))

    form = PostModelForm()
    return render(request, 'add_blog.html', {"form" : form})





