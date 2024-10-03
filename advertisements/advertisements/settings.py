"""
Django settings for advertisements project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os

from pathlib import Path

from .config import config

from .secrets import SECRET_KEY, external_ip, internal_ip, dns_ip, time_zone


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config.DEBUG
DEBUG = True


ALLOWED_HOSTS = [
    '127.0.0.1',
    '127.0.0.1.8000',
    'localhost:8000',
    internal_ip,
    external_ip,
    dns_ip,
    '*',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'application.apps.AppAdvertisementsConfig',

    'main',
    'user',
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

ROOT_URLCONF = 'advertisements.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            Path.joinpath(BASE_DIR, "templates")
        ],
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

WSGI_APPLICATION = 'advertisements.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../data/db.sqlite3',
        # "USER": "",
        # "PASSWORD": "",
        # "HOST": "127.0.0.1:8000",
        # "PORT": "",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Смена часового пояса
# TIME_ZONE = 'UTC'
TIME_ZONE = time_zone

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# BETA STATICS
# STATIC_URL = 'static/'
# STATIC_ROOT = Path.joinpath(BASE_DIR, 'static/')
#
# STATIC_DIRS = [
#     Path.joinpath(BASE_DIR, 'static')
# ]
#
# MEDIA_URL = 'media/'
# MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media/')
#
# MEDIA_DIRS = [
#     Path.joinpath(BASE_DIR, 'media')
# ]
#
# STATICFILES_URL = 'staticfiles/'
# STATICFILES_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#
# STATICFILES_DIRS_ROOT = [
#     Path.joinpath(BASE_DIR, 'staticfiles')
# ]

# STATIC
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

STATIC_DIRS_ROOT = [
    os.path.join(BASE_DIR, 'static/')
]

# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_DIRS = [
    os.path.join(BASE_DIR, 'media/')
]

MEDIA_DIRS_ROOT = [
    os.path.join(BASE_DIR, 'media/')
]

# STATICFILES
STATICFILES_URL = '/staticfiles/'
STATICFILES_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles/'),
]

STATICFILES_DIRS_ROOT = [
    os.path.join(BASE_DIR, 'staticfiles/')
]

# Включаем обслуживание медиа-файлов
# if DEBUG:
#     INSTALLED_APPS += ['django.contrib.staticfiles']
#     STATIC_URL = '/static/'
#     STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# else:
#     MIDDLEWARE += ['django.middleware.common.CommonMiddleware']
#     STATIC_URL = '/static/'
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#     MEDIA_URL = '/media/'
#     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Включаем обслуживание статических файлов
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
