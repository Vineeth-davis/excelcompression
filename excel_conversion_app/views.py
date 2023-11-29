import os
import time

import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadForm
import datetime
from django.utils import timezone
import subprocess
from datetime import timedelta

from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler

# from excel_conversion_project.jobs import updater
from .tasks import *
sched = BlockingScheduler()


#import background
def run_process_tasks_background():
    subprocess.run(["python", "manage.py", "process_tasks"])

from celery import shared_task



def process_and_generate_excel_background(file, file_type, selected_columns, column_names, file_path,schedule=timezone.now()):
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

    return excel_file_path



def loopfunc(schedule_time):

    current_time = datetime.now()
    if current_time == schedule_time:
        return True
    else:
        loopfunc(loopfunc(schedule_time))


def process_and_generate_excel(file, file_type, selected_columns, column_names, file_path):
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

    return excel_file_path

def schedule_task(file, file_type, selected_columns, column_names, file_path):
    try:
        excel_file_path = process_and_generate_excel(file, file_type, selected_columns, column_names, file_path)
        if excel_file_path:
            print("Excel file created successfully!")
            return 'success'
        else:
            print("Error creating Excel file.")
            return 'error'
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'error'

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                #file_path = form.cleaned_data['file_path']
                file_type = form.cleaned_data['file_type']
                selected_columns_str = form.cleaned_data['selected_columns']
                selected_columns = [int(column.strip()) for column in selected_columns_str.split(',')]
                column_names = form.cleaned_data['column_names'].split(',') if form.cleaned_data['column_names'] else None
                new_file_name = form.cleaned_data['new_file_name']
                output_file_path = form.cleaned_data['output_file_path']
                schedule_time = form.cleaned_data['schedule_time']
                file = request.FILES['file']
                schedule_time = form.cleaned_data['schedule_time']

                file_path = os.path.join(output_file_path, new_file_name)

                if schedule_time:

                    scheduled_datetime = timezone.datetime.combine(timezone.now().date(), schedule_time)
                    print("scheduled_datetime::::",scheduled_datetime)
                    # sched.add_job(process_and_generate_excel(file, file_type, selected_columns, column_names, file_path), 'date', run_date='2009-11-06 16:30:05', args=['text'])
                    excel_file_path = run_task(scheduled_datetime)

                    #return JsonResponse({'status': 'success', 'message': 'Excel file created successfully!'})
                    #excel_file_path = sched.add_job(process_and_generate_excel(file, file_type, selected_columns,
                    # @sched.scheduled_job('date', run_date=str(scheduled_datetime))
                    # def scheduled_job():
                    #     nonlocal excel_file_path  # Use the nonlocal keyword to modify the outer function's variable
                    #     excel_file_path = process_and_generate_excel(file, file_type, selected_columns, column_names,
                    #                                                  file_path)
                    #     result = schedule_task(file, file_type, selected_columns, column_names, file_path)
                    #     print(result)
                    # schedule_time = timezone.datetime.strptime(schedule_time, "%H:%M").time()
                    # print("-------------schedule_time-----------", type(schedule_time))
                    # i = True
                    # while i:
                    #     current_time = timezone.now().time()
                    #     print("")
                    #     current_time = timezone.now().strptime(current_time, "%H:%M").time()
                    #
                    #     print("current time:::::::::::::",current_time)
                    #
                    #     if current_time >= schedule_time:
                    #         print("done")
                    #         excel_file_path = process_and_generate_excel(file, file_type, selected_columns, column_names, file_path)
                    #         i = False
                    #     else:
                    #         pass
                    #

                    # current_time = timezone.now()
                    # if current_time > schedule_time:
                    #     scheduled_datetime = timezone.datetime.combine(timezone.now() + timedelta(days=1), schedule_time)
                    # else:
                    #     scheduled_datetime = timezone.datetime.combine(timezone.now().date(), schedule_time)
                    #
                    # print("-------------schedule_time-----------",scheduled_datetime)
                    #
                    # excel_file_path = process_and_generate_excel_background((file, file_type, selected_columns, column_names, file_path),schedule=schedule_time)

                else:
                    excel_file_path = process_and_generate_excel(file, file_type, selected_columns, column_names, file_path)
                if excel_file_path:
                    return JsonResponse({'status': 'success', 'message': 'Excel file created successfully!'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Error creating Excel file.'})
        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'status': 'error', 'message': 'Error processing the file.'})
    else:
        form = FileUploadForm()

    return render(request, 'upload_file.html', {'form': form})


