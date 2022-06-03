from django.shortcuts import render,get_object_or_404,redirect,resolve_url
from .models import  Post,comment
from .forms import Commentform,Postform
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def postlist(request):
    context= { 'post':Post.objects.all(),}
    return render(request,'index.html',context)

def comment_detile(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method=='POST':
       form= Commentform(request.POST)

       if form.is_valid():
          obj= form.save(commit=False)
          obj.post=post
          obj.save()

          return redirect('post',pk=post.pk)
    else:
        form= Commentform()

    context={
        'post':post,
        'form':form}
    return render(request,'post.html',context)

@login_required(login_url='/accounts/login')
@permission_required("post.add", login_url="/accounts/login")
def add(request ):

    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)

        if form.is_valid():
            post = Post(user=request.user, **Postform.cleaned_data)
            post = form.save()
            return redirect(resolve_url("home"))
    form = Postform()
    return render(request, 'add_post.html', {"form" : form})