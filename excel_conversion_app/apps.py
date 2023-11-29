from django.apps import AppConfig
import os
scheduled_time = os.environ.get('SCHEDULED_TIME')

class ExcelConversionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'excel_conversion_app'

    # def ready(self):
    #     from .tasks import run_task
    #     scheduled_time = os.environ.get('SCHEDULED_TIME')
    #     run_task(scheduled_time)
