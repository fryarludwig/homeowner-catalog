from django.http import HttpResponse
from django.shortcuts import render
# from material.frontend import forms
from django import forms

from django.views import View

from homeowner_catalog.login.forms import LoginForm


class LoginFormProvided(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    keep_logged = forms.BooleanField(required=False, label="Keep me logged in")


class LoginHelper(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'login.html', {'form': LoginForm()})
        else:
            return render(request, 'home.html', {'user': request.user})
