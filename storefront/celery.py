import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','storefront.settings')
# this means we're setting the environment variable DJANGO_SETTINGS_MODULE to settings of storefront project.

celery = Celery()
celery.config_from_object('django.conf:settings',namespace='CELERY')
# it looks where celery can find configuration varible. which is in django.conf module load the settings. 
# namespace means all our configuraions starts with CELERY.
celery.autodiscover_tasks()
