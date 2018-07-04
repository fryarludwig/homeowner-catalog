

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', min_length=4, max_length=64)
    password = forms.CharField(label='Password', min_length=4, max_length=64)
