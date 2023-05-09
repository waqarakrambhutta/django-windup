from time import sleep
from storefront.celery import celery # this is the celery we created in storefront project.

@celery.task
def notify_customer(message):
    print('Sending 10k emails...')
    print(message)
    sleep(10)
    print('Emails were successfully sent!')