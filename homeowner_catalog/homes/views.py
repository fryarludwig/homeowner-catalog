from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
# from material.frontend import forms
from django import forms

from django.views import View

from homeowner_catalog.domain.models import Home, Account
from homeowner_catalog.domain.utils import unwrap_lazy_object
from homeowner_catalog.homes.forms import HomeForm
from login.forms import LoginForm


class HomeHelper(View):
    def get(self, request, id=None, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'login.html', {'form': HomeForm()})
        elif id:
            try:
                home = Home.objects.get(pk=id)
                return render(request, 'homes.html', {'user': request.user,
                                                      'home': home})
            except ObjectDoesNotExist:
                return render(request, 'dashboard.html', {'user': request.user})
        else:
            return render(request, 'homes.html', {'user': request.user,
                                                  'form': HomeForm()})

    def post(self, request):
        form = HomeForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                try:
                    new_home = form.save(commit=False)
                    new_home.owner = Account.objects.get(pk=request.user.id)
                    # new_home.owner = unwrap_lazy_object(request.user)
                    new_home.save()
                    form.save_m2m()
                    print(request, "Thanks for creating a home. You are now ready to start.")
                    return render(request, 'homes.html', {'user': request.user,
                                                          'home': new_home})
                except Exception as e:
                    print('Some error occurred in the home building process: {}'.format(e))
                    return render(request, 'homes.html', {'user': request.user,
                                                          'error': e})
        return render(request, 'login.html', {'form': LoginForm()})
