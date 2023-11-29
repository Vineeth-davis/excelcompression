from datetime import datetime
from .jobs import my_task
# from excel_conversion_project.excel_conversion_app.views import process_and_generate_excel
# from apscheduler.scheduler.backgrounds import BackgroundScheduler
# from .jobs import schedule_task
#
#


from apscheduler.schedulers.background import BlockingScheduler,BackgroundScheduler

def start(hour,minutes,seconds):
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_task, 'cron', hour=hour, minute=minutes, second=seconds)
    scheduler.start()



# def run_task(scheduled_datetime):
#     if scheduled_datetime:
#         scheduler= BackgroundScheduler()
#         # scheduler.add_job(schedule_task,'interval',seconds=20)
#         scheduler.add_job(process_and_generate_excel, 'cron', hour=18, minute=50, second=0)
#
#         scheduler.start()
#         print(f"scheduled task {scheduled_datetime}")

# count = 0

# def job_function():
#     print("job executing")
#     global count, scheduler
#
#     # Execute the job till the count of 5
#     count = count + 1
#     if count == 1:
#         scheduler.remove_job('my_job_id')
#
#
# scheduler = BlockingScheduler()
# scheduler.add_job(job_function, 'interval', seconds=1, id='my_job_id')
#
#
# scheduler.start()
#


#
# import os
# import time
# import pandas as pd
# from django.http import JsonResponse
# from django.shortcuts import render
# from .forms import FileUploadForm
# import datetime
# from django.utils import timezone
# import subprocess
# from datetime import timedelta
# from datetime import date
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# sched = BlockingScheduler()
#
# def process_and_generate_excel(file, file_type, selected_columns, column_names, file_path):
#     if file_type == 'csv':
#         df = pd.read_csv(file, sep=',')
#     elif file_type == 'tsv':
#         df = pd.read_csv(file, sep='\t')
#     else:
#         return None
#     if not column_names:
#         default_column_names = list(df.columns[selected_columns])
#         column_names = default_column_names
#
#     df_selected = df.iloc[:, selected_columns]
#     df_selected.columns = column_names
#     excel_file_path = f'{file_path}.xlsx'
#     df_selected.to_excel(excel_file_path, index=False)
#
#     return excel_file_path
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES)
#         try:
#             if form.is_valid():
#                 file_type = form.cleaned_data['file_type']
#                 selected_columns_str = form.cleaned_data['selected_columns']
#                 selected_columns = [int(column.strip()) for column in selected_columns_str.split(',')]
#                 column_names = form.cleaned_data['column_names'].split(',') if form.cleaned_data['column_names'] else None
#                 new_file_name = form.cleaned_data['new_file_name']
#                 output_file_path = form.cleaned_data['output_file_path']
#                 schedule_time = form.cleaned_data['schedule_time']
#                 file = request.FILES['file']
#                 schedule_time = form.cleaned_data['schedule_time']
#
#                 file_path = os.path.join(output_file_path, new_file_name)
#
#                 if schedule_time:
#                     scheduled_datetime = timezone.datetime.combine(timezone.now().date(), schedule_time)
#                     print("scheduled_datetime::::", scheduled_datetime)
#                     sched.add_job(
#                         process_and_generate_excel(file, file_type, selected_columns, column_names, file_path), 'date',
#                         run_date='2009-11-06 16:30:05', args=['text'])
#                     excel_file_path = sched.start()
#                 else:
#                     excel_file_path = process_and_generate_excel(file, file_type, selected_columns, column_names, file_path)
#                 if excel_file_path:
#                     return JsonResponse({'status': 'success', 'message': 'Excel file created successfully!'})
#                 else:
#                     return JsonResponse({'status': 'error', 'message': 'Error creating Excel file.'})
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             return JsonResponse({'status': 'error', 'message': 'Error processing the file.'})
#     else:
#         form = FileUploadForm()
#
#     return render(request, 'upload_file.html', {'form': form})


# def schedule_task(file, file_type, selected_columns,column_names, file_path):
#     try:
#         excel_file_path = process_and_generate_excel(file, file_type, selected_columns,column_names, file_path)
#         if excel_file_path:
#             print("Excel file created successfully!")
#             return JsonResponse(
#                 {'status': 'success', 'message': 'Excel file created successfully!'})
#         else:
#             print("Error creating Excel file.")
#             return JsonResponse({'status': 'error', 'message': 'Error processing the file.'})
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return JsonResponse({'status': 'error', 'message': 'Error processing the file.'})