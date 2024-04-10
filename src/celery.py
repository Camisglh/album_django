from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
CELERY_BEAT_INTERVAL = 30
CELERY_ROUTES = {
    "card.tasks.add_photo": "worker1",
    "card.tasks.process_photo": "worker2",
}
app = Celery("src")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
