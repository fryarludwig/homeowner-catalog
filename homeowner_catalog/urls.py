"""homeowner_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, register_converter
from django.views.generic import RedirectView

from homeowner_catalog import converters, accounts
from homeowner_catalog.login.views import LoginForm
from homeowner_catalog.overview.views import index
from material.frontend import urls as frontend_urls

register_converter(converters.DateConverter, 'date')

urlpatterns = [
    # authentication urls
    # path('auth', include('rest_framework_signature.urls')),
    path('admin/', admin.site.urls),
    path('login', LoginForm, name='login'),
    # path('account', accounts, name='account'),

    path('', include(frontend_urls)),
]

