from django import forms


class UserFormLogin(forms.Form):

    username = forms.CharField( label="Your username", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)