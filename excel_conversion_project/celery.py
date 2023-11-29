
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_conversion_project.settings')

app = Celery('excel_conversion_project')

app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object('settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# celery=Celery(include=[ 'tasks.chatterbox' ])
#
# # import celery config file
# celery.config_from_object('celeryconfig')
#
# if __name__ == '__main__':
#     celery.start()