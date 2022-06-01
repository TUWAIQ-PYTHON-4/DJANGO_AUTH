from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post, Comment
from .forms import PostModelForm, CommentForm



def index(request: HttpRequest):
    blog_posts = Post.objects.all()
    context = {'posts': blog_posts}
    response = render(request, 'index.html', context)
    return response


@login_required(login_url='/accounts/login')
@permission_required("post.add_post", login_url="/accounts/login")
def add_post(request):
    if request.method == "POST":
        postModelForm = PostModelForm(request.POST, request.FILES)

        if postModelForm.is_valid():
            post = Post(user=request.user, **postModelForm.cleaned_data)
            post.save()
            return redirect('index')
    form = PostModelForm()
    return render(request, 'add_post.html', {'form': form})


def post_detail(request: HttpRequest, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            added_comment = Comment(post=post, first_name=commentform.cleaned_data["first_name"],
                                    content=commentform.cleaned_data["content"],
                                    email=commentform.cleaned_data["email"])
            added_comment.save()
        else:
            print(commentform.errors)

    context = {"post": post, "form": CommentForm()}
    return render(request, 'detail.html', context)