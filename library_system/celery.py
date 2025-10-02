import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

BEAT_BEAT_SCHEDULE = {
    'library.tasks.send_loan_notification': {
        'queue': 'default'
    }
}

TASK_ROUTES = {
    'library.tasks.check_overdue_loans': {
        'schedule': crontab(minute=0, hour=0)
    }
}
