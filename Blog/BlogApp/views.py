from django.http import HttpRequest
from django.shortcuts import render
from .models import Post, Comments
from .forms import CommentsForm, PostsForm
from django.contrib.auth import authenticate, login


def posts_list(request: HttpRequest):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, 'home.html', context)


def post_detail(request: HttpRequest, id: int):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comments(post=post, first_name=comment_form.cleaned_data["first_name"],
                                     content=comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)

    context = {'post': post, "form": CommentsForm()}
    return render(request, 'post_details.html', context)


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
