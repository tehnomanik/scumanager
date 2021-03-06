"""
Django settings for home project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.conf.locale.en import formats as en_formats
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$g4gtk+bp$sylr8%l#5zwnq^cme*)8k_l_o(7&bifq^=h-fb+='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'front',
    'players',
    'django_filters',
    'bootstrapform',
    'settings'
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

ROOT_URLCONF = 'home.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'home.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-hr'

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_INPUT_FORMATS = [
    '%d.%m.%Y', #'%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    #'%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    #'%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    #'%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    #'%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
]

DATETIME_INPUT_FORMATS = [
    '%d.%m.%Y %H:%M:%S',     # '2006-10-25 14:30:59'
    #'%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    #'%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    #'%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    #'%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    #'%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    #'%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    #'%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    #'%m/%d/%y %H:%M',        # '10/25/06 14:30'
]

#DATETIME_FORMAT = 'Y-m-d H:i:sO'
#DATE_FORMAT = 'Y-m-d'

#DATE_INPUT_FORMATS = ('%d/%m/%Y','%d-%m-%Y','%Y-%m-%d')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/img/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]