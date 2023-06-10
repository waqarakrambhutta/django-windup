import os
import dj_database_url
from .common import *


DEBUG = False # If debug is off them we need to add the setting allowed hosts below.

SECURITY_KEY = os.environ('SECURITY_KEY')

ALLOWED_HOSTS = ['mirror-storefront.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config() 
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