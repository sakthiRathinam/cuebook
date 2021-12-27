from __future__ import absolute_import,unicode_literals
import os
from django.apps import apps
from celery import Celery
from coresingle.settings import CELERY_IMPORTS


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coresingle.settings')

app = Celery('coresingle',include=CELERY_IMPORTS)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])