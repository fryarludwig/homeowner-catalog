from django.http import HttpResponse
from django.shortcuts import render
# from material.frontend import forms
from django import forms

# def login(request):
#     return render(request, 'login.html')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    keep_logged = forms.BooleanField(required=False, label="Keep me logged in")
