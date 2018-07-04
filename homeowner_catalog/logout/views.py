from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.auth import logout

from django.views import View


class LogoutHelper(View):
    def get(self, request, *args, **kwargs):
        result = logout(request)
        return render(request, 'home.html', {'result': result})
