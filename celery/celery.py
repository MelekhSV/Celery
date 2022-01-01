import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery.settings')

app = Celery('send_email')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-spam-every-10-minute':{
        'task': 'main.tasks.send_beat_email',
        'schedule': crontab(minute='*/10')
    }
}