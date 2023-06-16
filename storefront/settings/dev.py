from .common import *

DEBUG = True
# SECURITY WARNING: don't run with debug turned on in production!

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'
# SECURITY WARNING: keep the secret key used in production secret!

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'waqar123!@#',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "TIMEOUT": 10*60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/1'



EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = '' # due to fake SMTP the host user is empty.
EMAIL_HOST_PASSWORD = '' # similarly password is also empty.
EMAIL_PORT = 2525 # by default it used 25, due to fake SMTP we use 2525
DEFAULT_FROM_EMAIL = 'waqar@domian.com'
# we use the password in the envionment variable due to security problem. which we'll learn in production.


