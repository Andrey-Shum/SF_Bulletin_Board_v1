import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BulletinBoard.settings')

app = Celery('BulletinBoard')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Настройка периодических задач
app.conf.beat_schedule = {
    'send-daily-newsletter': {
        'task': 'appSubscriptions.tasks.send_newsletters',
        'schedule': crontab(hour=8, minute=0),  # Каждый день в 8:00
    },
} 