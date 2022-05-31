
from django.shortcuts import render, redirect, resolve_url
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required



def index(request):
    all_posts= Post.objects.all()

    return render(request, 'blog/index.html', {'posts': all_posts })

@login_required(login_url="/accounts/login")
def add_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect(resolve_url("blogs:index"))

    else:
        post_form = PostForm()
    return render(request, 'blog/add_post.html', {'form': post_form})


def post_detail(request, post_id):
    post_info = Post.objects.get(pk=post_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(name=comment_form.cleaned_data["name"],comment=comment_form.cleaned_data["content"], post=post_info)
            added_comment.save()
        else:
            print(comment_form.errors)

    return render(request, 'blog/detail.html', {"post": post_info, "form": CommentForm()})

