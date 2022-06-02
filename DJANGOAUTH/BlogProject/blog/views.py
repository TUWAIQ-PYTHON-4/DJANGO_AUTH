from django.http import HttpRequest
from django.shortcuts import render, redirect, resolve_url
from .forms import PostModelForm, CommentForm
from .models import Post, Comment


def index(request : HttpRequest):

    post = Post.objects.all()

    context = {"posts": post, "display": True}

    if request.user.is_authenticated:
        context["user"] = request.user
        print("is authenticated")
    else:
        return redirect(resolve_url("accounts:login"))





def add_blog(request : HttpRequest):


    if not request.user.has_perm("blog.add_blog"):
        return redirect(resolve_url("accounts:login"))

    if request.method == 'POST':
        postModelForm = PostModelForm(request.POST, request.FILES)

        if postModelForm.is_valid():
            #add model
            blog = Post(user=request.user,  **postModelForm.cleaned_data)
            blog.save()
            return redirect(resolve_url("blog:index"))

    form = PostModelForm()
    return render(request, 'add_blog.html', {"form" : form})


def blog_detail(request: HttpRequest, blog_id):
    blog = Post.objects.get(pk=blog_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(blog=blog, title=comment_form.cleaned_data["title"],
                                    content=comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)

    context = {"blog": blog, "form": CommentForm()}

    return render(request, 'book_detail.html', context)


