import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nti_games.settings')

celery_app = Celery('nti_games')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
