from django.apps import AppConfig



class ExcelConversionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'excel_conversion_app'
    #
    def ready(self):
        from .tasks import run_task
        run_task()
