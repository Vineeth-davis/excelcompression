from django.conf import settings
# from excel_conversion_project.excel_conversion_app.views import process_and_generate_excel
#
import json
import os
import pandas as pd
from ..excel_conversion_app.views import process_and_generate_excel


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

def my_scheduled_task():
    scheduled_time = os.environ.get('SCHEDULED_TIME')
    file = os.environ.get('FILE')
    file_type = os.environ.get('FILE_TYPE')
    selected_columns = os.environ.get('SELECTED_COLUMNS')
    column_names = os.environ.get('COLUMN_NAMES')
    file_path = os.environ.get('FILE_PATH')
    excel_file_path = process_and_generate_excel(file, file_type, selected_columns, column_names, file_path)
    print("scheduled job done")
    return excel_file_path