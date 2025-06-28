import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJANGO_INTERN_APP.settings')

app = Celery('DJANGO_INTERN_APP')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
#6379