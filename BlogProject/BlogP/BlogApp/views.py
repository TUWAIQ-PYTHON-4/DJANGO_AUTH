from django.shortcuts import render, resolve_url, redirect
from django.template import response
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            post_list = Post.objects.all()
            print()
            context = {"Posts": post_list}
            return render(request, 'index.html', context)
    post_list = Post.objects.all()
    context = {"Posts": post_list}
    return render(request, 'index.html', context)



def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(resolve_url("/index"))
    form = PostForm()
    return render(request, 'add.html', {"form": form})


def comment(request ,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(post=post, first_name=comment_form.cleaned_data["first_name"],content=comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)
    context = {"post" : post, "form" : CommentForm()}
    return render(request, 'detail.html', context)


def my_view(request):
    if not request.user.is_authenticated:
        return render(request, 'add.html')
