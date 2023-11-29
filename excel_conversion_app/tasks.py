# from celery import shared_task
#
# @shared_task(bind=true)


from apscheduler.schedulers.background import BlockingScheduler,BackgroundScheduler

from .views import process_and_generate_excel


def run_task(scheduled_datetime):
    if scheduled_datetime:
        scheduler= BackgroundScheduler()
        # scheduler.add_job(schedule_task,'interval',seconds=20)
        scheduler.add_job(process_and_generate_excel, 'cron', hour=12, minute=50, second=0)

        scheduler.start()
        print(f"scheduled task {scheduled_datetime}")