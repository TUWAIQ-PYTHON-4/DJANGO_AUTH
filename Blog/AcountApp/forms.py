from django import forms


class UserForm(forms.Form):

    username = forms.CharField( label="Your username", max_length=60)
    email = forms.CharField(label="Your email", max_length=70)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)

class UserFormLogin(forms.Form):

    username = forms.CharField( label="Your username", max_length=60)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)
