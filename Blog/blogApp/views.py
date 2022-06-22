from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

# Create your views here.
from .models import Post, Comment
from .forms import PostForm, push_post
from django.http import HttpResponseRedirect


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/base.html', context)


def post_infor(request, id):
    post_infor = Post.objects.get(id=id)
    post_commint = Comment.objects.filter(post=post_infor)
    context = {'post_infor': post_infor, 'post_commint': post_commint}
    return render(request, 'blog/show.html', context)


def push_post(request):
    submitted = False
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/push_post?submitted=True')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'blog/add_post.html', {'form': form, 'submitted': submitted})
