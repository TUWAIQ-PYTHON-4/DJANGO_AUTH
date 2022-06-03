from django.shortcuts import render,redirect, resolve_url, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def list_post(request):
    context={"post": Post.objects.all(),}
    return render (request,'index.html',context)

@login_required(login_url="login")
@permission_required("blogApp.add_post", login_url="login")
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(resolve_url("home"))
        else:
            print(form.errors)
    form = PostForm()
    return render(request, 'add-post.html', {"form" : form})
@login_required(login_url="/account/login")
def comment_detile(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method=='POST':
       form= CommentForm(request.POST)

       if form.is_valid():
          obj= form.save(commit=False)
          obj.post=post
          obj.save()

          return redirect('post',pk=post.pk)
    else:
        form= CommentForm()

    context={
        'post':post,
        'form':form}
    return render(request,'post.html',context)

