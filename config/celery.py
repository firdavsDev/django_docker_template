import os

import cronitor.celery

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery monitoring (https://cronitor.io/)
cronitor.api_key = os.environ["CRONITOR_API_KEY"]
cronitor.celery.initialize(app)
