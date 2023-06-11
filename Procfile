release: pipenv run upgrade
release: python manage.py migrate
web: gunicorn storefront.wsgi
worker: celery -A storefront worker
