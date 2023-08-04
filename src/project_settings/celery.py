import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_settings.settings")

app = Celery("project_settings")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-mailings-every-1-hour": {
        "task": "mailings.tasks.send_message",
        "schedule": crontab(minute=0, hour="*/1,9-22"),
        # "schedule": crontab(minute="*/1"),
    },
}
