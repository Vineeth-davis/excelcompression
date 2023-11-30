from datetime import datetime
from .jobs import my_task,my_scheduled_task
# from excel_conversion_project.excel_conversion_app.views import process_and_generate_excel
# from apscheduler.scheduler.backgrounds import BackgroundScheduler
# from .jobs import schedule_task


from apscheduler.schedulers.background import BackgroundScheduler

def start(hour,minutes,seconds):
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_scheduled_task, 'cron', hour=hour, minute=minutes, second=seconds)
    scheduler.start()

