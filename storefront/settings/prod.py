import os
import dj_database_url
from .common import *


DEBUG = False # If debug is off them we need to add the setting allowed hosts below.

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['storefrontapp-68a745ebc45c.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600) 
}

REDIS_URL = os.environ['REDIS_URL']
CELERY_BROKER_URL = REDIS_URL
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "TIMEOUT": 10*60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']