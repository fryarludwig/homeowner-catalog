
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, JsonResponse, HttpResponseServerError
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

