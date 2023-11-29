from django.conf import settings
# from excel_conversion_project.excel_conversion_app.views import process_and_generate_excel
#
import json
import pandas as pd
def my_task(file, file_type, selected_columns, column_names, file_path):
    if file_type == 'csv':
        df = pd.read_csv(file, sep=',')
    elif file_type == 'tsv':
        df = pd.read_csv(file, sep='\t')
    else:
        return None
    if not column_names:
        default_column_names = list(df.columns[selected_columns])
        column_names = default_column_names

    df_selected = df.iloc[:, selected_columns]
    df_selected.columns = column_names
    excel_file_path = f'{file_path}.xlsx'
    df_selected.to_excel(excel_file_path, index=False)
    print("task is doen")

    return excel_file_path
from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler


# sched = BlockingScheduler()
#
# count = 0
# def my_job():
#
#     print(text)
#     # global count, sched
#     #
#     # # Execute the job till the count of 5
#     # count = count + 1
#     # if count == 1:
#     #     sched.remove_job()
#
# # The job will be executed on November 6th, 2009
# sched.add_job(my_job, 'date', run_date='2023-11-29 01:06:55', args=['text'])
#
# sched.start()
