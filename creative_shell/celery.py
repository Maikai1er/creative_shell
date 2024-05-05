from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creative_shell.settings')
# KOSTYL, doesn't work without this line
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('creative_shell')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
