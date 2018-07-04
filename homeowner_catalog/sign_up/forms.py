

from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    # username = forms.CharField(label='Username', min_length=4, max_length=64)
    # password = forms.CharField(label='Password', min_length=4, max_length=64,
    #                            widget=forms.PasswordInput())
    email = forms.EmailField(label='Email')

