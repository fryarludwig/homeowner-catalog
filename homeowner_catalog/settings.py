"""
Django settings for homeowner_catalog project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import json
import os
from configurations import Configuration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

class Base(Configuration):
    # Loads settings configuration data from settings.json file
    data = {}
    settings_path = os.path.join(BASE_DIR, 'homeowner_catalog', 'settings.json')
    try:
        with open(settings_path) as data_file:
            data = json.load(data_file)
    except IOError:
        print('You need to setup the settings data file, file {}:\n '
              '(see instructions in base.py file.)'.format(settings_path))
        exit(1)

    # SECURITY WARNING: keep the secret key used in production secret!
    try:
        SECRET_KEY = data["secret_key"]
    except KeyError:
        print("The secret key is required in the settings.json file.")
        exit(1)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['testserver', '127.0.0.1', 'localhost']

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'homeowner_catalog.apps.RentplusApiConfig',
        'material',
        'material.frontend',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'homeowner_catalog.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    # WSGI_APPLICATION = 'wsgi.application'
    WSGI_APPLICATION = 'homeowner_catalog.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases
    DATABASES = {}
    for database in data['databases']:
        DATABASES[database['type']] = {
            'ENGINE': database['engine'],
            'NAME': database['name'],
            'USER': database['user'] if 'user' in database else '',
            'PASSWORD': database['password'] if 'password' in database else '',
            'HOST': database['host'] if 'host' in database else '',
            'PORT': database['port'] if 'port' in database else '',
            'OPTIONS': database['options'] if 'options' in database else {},
            'TEST': database['test'] if 'test' in database else {},
        }

    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # rest_framework config
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'djangorestframework.authentication.TokenAuthentication',
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        )
    }

    # set test runner to nose
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

    # Internationalization
    # https://docs.djangoproject.com/en/2.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    # AUTH_USER_MODEL = 'accounts.User'

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_URL = '/static/'

    # All settings common to all environments
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


class Local(Base):
    pass


class Dev(Base):
    pass


class Prod(Base):
    pass