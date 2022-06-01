from django import forms


class UserFormLogin(forms.Form):

    username = forms.CharField( label=" username", max_length=64)
    password = forms.CharField(label=" password", widget=forms.widgets.PasswordInput) 
