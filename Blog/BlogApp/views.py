from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ComForm, PostForm


# Create your views here.


def index(request: HttpRequest):
    all_posts = Post.objects.all()
    context = {'posts': all_posts}
    response = render(request, 'index.html', context)
    return response


@login_required(login_url='/accounts/login')
@permission_required("post.add_post", login_url="/accounts/login")
def add_post(request):
    if request.method == "POST":
        postForm = PostForm(request.POST, request.FILES)

        if postForm.is_valid():
            post = Post(user=request.user, **postForm.cleaned_data)
            post.save()
            return redirect('index')
    form = postForm()
    return render(request, 'add_post.html', {'form': form})


def post_detail(request: HttpRequest, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        comform = ComForm(request.POST)
        if comform.is_valid():
            add_comment = Comment(post=post, first_name=comform.cleaned_data["first_name"],
                                  content=comform.cleaned_data["content"],
                                  email=comform.cleaned_data["email"])
            add_comment.save()
        else:
            print(comform.errors)

    context = {"post": post, "form": ComForm()}
    return render(request, 'detail.html', context)
