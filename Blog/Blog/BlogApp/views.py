from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect, resolve_url
from .models import Post, Comment
from .forms import addForm, addComment


# Create your views here.

def index(request: HttpRequest):
    all_item = Post.objects.all()
    context = {'all_item': all_item, 'display': True}

    return render(request, 'index.html', context)


def detail(request: HttpRequest, post_id):
    post = Post.objects.get(pk=post_id)

    session_content = request.session.get("detail", None)
    if request.method == "POST":
        comment_form = addComment(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(first_name=request.user, **comment_form.cleaned_data)
            added_comment.save()

    context = {'post': post, 'added_comment': added_comment}

    return render(request, 'detail.html', context)


@login_required(login_url="/accounts/login")
def add_blog(request: HttpRequest):
    if not request.user.has_perm("movies.add_movie"):
        return redirect(resolve_url("accounts:login"))

    if request.method == 'POST':
        AddForm = addForm(request.POST, request.FILES)

        if AddForm.is_valid():
            # add model
            post = Post(user=request.user, **AddForm.cleaned_data)
            post.save()
            return redirect(resolve_url("index"))

    form = addForm()
    return render(request, 'add.html', {"form": form})
