
from django import forms
# from .models import category, subcategory



class UploadForm(forms.Form):

    excel_file = forms.FileField(
        error_messages={'required': 'Excel upload is required.'},
        label='Upload excel',
        required=True,
        max_length=200,
        widget=forms.ClearableFileInput(attrs={'id': "excel"}))


