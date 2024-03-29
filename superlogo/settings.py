"""
Django settings for superlogo project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from django.contrib.messages import constants as messages
import os
from pathlib import Path
import dj_database_url
import environ
env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bni-q+a&4eggvue+&l%__^n#q%-hlti_=sc-u1ff0joram2yb@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['172.31.128.1','192.168.101.10', '[::1]','www.algotrde.com','testserver', '127.0.0.1', 'http://localhost/','localhost','algotrde.com','https://algotrde.com','http://algotrde.com','34.100.183.27','optionperks.com','www.optionperks.com','0.0.0.0','34.100.184.223','35.200.212.177']

TIME_ZONE = 'Asia/Kolkata'
USE_TZ = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'home',
    'rest_framework',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'channels',
    'corsheaders',
    'django_celery_results',
    'django_celery_beat',
    'celery',
    "django_check_seo",
    'cms',
    'menus',
    'treebeard',
    'django.contrib.sitemaps'

    
]
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:80",
    "http://127.0.0.1:8001",
    "http://34.100.183.27",

    "https://www.algotrde.com",
    "https://optionperks.com",
    "http://optionperks.com",

    "http://www.algotrde.com",
    "http://www.optionperks.com",
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add this line to include AccountMiddleware

    

    
    
    
]
CSRF_TRUSTED_ORIGINS = ['https://*.algotrde.com', 'https://*.127.0.0.1' ,'https://*.optionperks.com',"http://*.34.100.183.27"]
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"

CORS_ORIGIN_WHITELIST = ["*"]
CROS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'superlogo.urls'
# AUTH_USER_MODEL = 'home.User'
# settings.py
AUTH_USER_MODEL = 'home.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'superlogo.wsgi.application'
ASGI_APPLICATION = 'superlogo.asgi.application'

CORS_ALLOW_CREDENTIALS = True
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': dj_database_url.parse(env('DATABASE_URL'))
# }

# Google Authentication

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    "django.contrib.auth.backends.ModelBackend",
]


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

from django.utils.translation import gettext_lazy as _

# Adjust LANGUAGE_CODE to match one of the entries in LANGUAGES


# Define LANGUAGES with proper language code and verbose name
LANGUAGES = (
        ('en-us', u'English (US)'),
        ('de', u'Deutsch'),
        ('en-gb', u'English (UK)'),
        ('es', u'Español'),
        ('fr', u'Français'),
        ('pt', u'Português'),
    )    


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")

]
STATIC_ROOT = 'home/static'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'




MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'optionperks@gmail.com'
EMAIL_HOST_PASSWORD = 'xojrleiasoimqyiw'
# xojrleiasoimqyiw

SITE_ID = 1

SOCIALACCOUNT_LOGIN_ON_GET = True

# settings.py
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': '929504800861-v6oo02qf7lvuch3sps866n1c1ktl78k2.apps.googleusercontent.com',
            'secret': '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',
            'key': '',
        },
        'AUTH_REDIRECT_URI': 'https://optionperks.com/accounts/google/login/callback/',
    }
}

LOGIN_REDIRECT_URL = '/'

# Channels Redis settings
CHANNEL_LAYERS = {
   'default': {
       'BACKEND': 'channels_redis.core.RedisChannelLayer',
       'CONFIG': {
           "hosts": [('localhost', 6379)],
       },
   },
}




# settings.py

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'



#celery-beat

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_IMPORTS = [
    'home.tasks',
]


ACCOUNT_DEFAULT_HTTP_PROTOCOL='http'

