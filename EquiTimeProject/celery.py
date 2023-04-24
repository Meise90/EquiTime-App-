from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EquiTimeProject.settings')

app = Celery('EquiTimeProject')
app.conf.enable_utc = False

app.conf.update(timezone='Europe/Warsaw')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings

app.conf.beat_schedule = {
    'clear-schedule-every-week': {
        'task': 'scheduleapp.tasks.delete_all_func',
        'schedule': crontab(hour=2, minute=0, day_of_week=1),
    }

}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')