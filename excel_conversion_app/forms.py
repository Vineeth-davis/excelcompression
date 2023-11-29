from django import forms

class FileUploadForm(forms.Form):
    #input_file_path = forms.CharField(max_length=255, label='Input File Path')
    file = forms.FileField(label='Input File')
    file_type = forms.ChoiceField(choices=[('csv', 'CSV'), ('tsv', 'TSV')], label='File Type')
    selected_columns = forms.CharField(max_length=255, label='Selected Columns (comma-separated)')
    column_names = forms.CharField(max_length=255, label='Column Names (comma-separated)', required=False)
    new_file_name = forms.CharField(max_length=255, label='New File Name')
    schedule_time = forms.TimeField(label='Scheduled Time', required=False, widget=forms.TimeInput(attrs={'type': 'time'}))

    output_file_path = forms.CharField(max_length=255, label='Output File Path')