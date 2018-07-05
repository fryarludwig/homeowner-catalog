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
from django.urls import path, include, register_converter, re_path
from django.views.generic import RedirectView

from homeowner_catalog import converters, accounts
from homeowner_catalog.homes.views import HomeHelper
from homeowner_catalog.login.views import LoginHelper
from homeowner_catalog.logout.views import LogoutHelper
from homeowner_catalog.overview.views import IndexHelper

from homeowner_catalog.sign_up.views import SignUpHelper
from material.frontend import urls as frontend_urls


register_converter(converters.DateConverter, 'date')

urlpatterns = [
    # authentication urls
    # path('auth', include('rest_framework_signature.urls')),
    path('admin/', admin.site.urls),
    path('homes', HomeHelper.as_view(), name='homes'),
    path('homes/<int:pk>', HomeHelper.as_view(), name='homes'),
    path('login', LoginHelper.as_view(), name='login'),
    path('logout', LogoutHelper.as_view(), name='logout_user'),
    path('resetPassword', LogoutHelper.as_view(), name='password_reset'),
    path('signup', SignUpHelper.as_view(), name='signup'),
    # path('account', accounts, name='account'),

    re_path('', include(frontend_urls)),
    re_path('', IndexHelper.as_view(), name='home'),
]

