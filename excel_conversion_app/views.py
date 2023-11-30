import os
import time

import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadForm
import datetime
from django.utils import timezone




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


def ready(hour,minutes,seconds):
    from ..jobs import updater
    updater.start(hour, minutes, seconds)


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                file_type = form.cleaned_data['file_type']
                selected_columns_str = form.cleaned_data['selected_columns']
                selected_columns = [int(column.strip()) for column in selected_columns_str.split(',')]
                column_names = form.cleaned_data['column_names'].split(',') if form.cleaned_data['column_names'] else None
                new_file_name = form.cleaned_data['new_file_name']
                output_file_path = form.cleaned_data['output_file_path']
                schedule_time = form.cleaned_data['schedule_time']
                file = request.FILES['file']

                file_path = os.path.join(output_file_path, new_file_name)

                if schedule_time:
                    scheduled_datetime = timezone.datetime.combine(timezone.now().date(), schedule_time)
                    print("scheduled_datetime::::",scheduled_datetime)
                    # excel_file_path = ready(schedule_time)
                    schedule_time = str(schedule_time)
                    #print(scheduled_time)
                    hour, minutes, seconds = map(str, schedule_time.split(':'))
                    print(hour, minutes, seconds)

                    os.environ.setdefault('SCHEDULED_TIME', schedule_time)

                    os.environ.setdefault('FILE_PATH', schedule_time)
                    os.environ.setdefault('COLUMN_NAMES', schedule_time)
                    os.environ.setdefault('SELECTED_COLUMNS', schedule_time)
                    os.environ.setdefault('FILE_TYPE', schedule_time)
                    os.environ.setdefault('FILE', schedule_time)

                    excel_file_path = ready(hour, minutes, seconds)
                    print("--excel_file_path---",excel_file_path)



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


