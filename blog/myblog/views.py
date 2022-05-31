from django.shortcuts import render , redirect , resolve_url

from .forms import UserFormLogin
from .models import Post, comment
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission , User



def index(request : HttpRequest):

    post_list = Post.objects.all()
    comment_list = comment.objects.all()
    context = {"comments": comment_list,"posts": post_list, "display": True}
    #context2 = {"comments": comment_list, "display": True}

    response = render(request, 'index.html', context )


    return response


def login_user(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserFormLogin(request.POST)

        if user_form.is_valid():

            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            authenticate_user = authenticate(request, username=username, password=password)

            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect(resolve_url('index'))
            else:
                return redirect(resolve_url('login'))

    return render(request, 'login.html', {'form': UserFormLogin()})
def add_post(requst: HttpRequest):
    if requst.user.is_authenticated and requst.user.has_perm("myblog.add_post"):
        return redirect(resolve_url('add_post'))
    else :
        return redirect(resolve_url('login'))