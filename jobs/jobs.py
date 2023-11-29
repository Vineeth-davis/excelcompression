# from django.conf import settings
from excel_conversion_project.excel_conversion_app.views import process_and_generate_excel
#
# import json

from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

count = 0
def my_job(text):

    print(text)
    # global count, sched
    #
    # # Execute the job till the count of 5
    # count = count + 1
    # if count == 1:
    #     sched.remove_job()

# The job will be executed on November 6th, 2009
sched.add_job(my_job, 'date', run_date='2023-11-29 01:06:55', args=['text'])

sched.start()
