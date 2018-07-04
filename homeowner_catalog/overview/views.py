from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.views import View

from homeowner_catalog.login.forms import LoginForm


class OverviewHelper(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {'request': request})
        #
        # if not request.user.is_authenticated:
        #     print('Redirecting user to login page from overview helper')
        #     return HttpResponseRedirect(request, 'login.html', {'form': LoginForm()})
        #     # return render(request, 'login.html', {'form': LoginForm()})
        # else:
        #     return render(request, 'home.html', {'user': request.user})
