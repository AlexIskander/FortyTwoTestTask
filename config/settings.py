# -*- coding: utf-8 -*-

"""
Django settings for forty_two_cups_coffy project.
"""
# import python
import os
from os.path import join, abspath, normpath, dirname

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+qpn%7d5yr_s&h2&gv#)#_r1tkf-gr62*fkajdun&7y9u52s2i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'bootstrap3',
    #'users',
]

MIDDLEWARE_CLASSES = [
    #'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'



WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.simmple',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = True
USE_TZ = True




MEDIA_ROOT = join(BASE_DIR, "site_media" )
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'
# Example: "/var/www/example.com/static/"
STATIC_ROOT = join(BASE_DIR, "site_assets")
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'


TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates' ),
)
