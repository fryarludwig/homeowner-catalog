from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render
# from material.frontend import forms
# from django import forms

# def login(request):
#     return render(request, 'login.html')
from django.views import View

from homeowner_catalog.sign_up.forms import SignUpForm


class SignUpHelper(View):
    def get(self, request, *args, **kwargs):
        print('Get request inside signup helper')
        if not request.user.is_authenticated:
            return render(request, 'signup.html', {'form': SignUpForm()})
        else:
            return render(request, 'index.html', {'user': request.user})

    def post(self, request, *args, **kwargs):
        print('Pretend we signed you up')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            print(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return render(request, 'index.html', {'user': new_user})
        else:
            return render(request, 'signup.html', {'form': SignUpForm(),
                                                   'error': 'Failed'})

