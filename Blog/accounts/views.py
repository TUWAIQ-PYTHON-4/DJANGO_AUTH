from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, resolve_url
from .forms import UserForm, UserFormLogin




def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(user_form.cleaned_data["username"],
                                                user_form.cleaned_data["email"],
                                                user_form.cleaned_data["password"])
            new_user.save()

            return redirect(resolve_url('blogs:index'))

    return render(request, 'accounts/register.html', {'form': UserForm()})


def login_user(request):
    if request.method == 'POST':
        user_form = UserFormLogin(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(resolve_url('blogs:index'))
    else:
        return redirect(resolve_url('accounts:login'))

    return render(request, 'accounts/login.html', {'form': UserFormLogin()})