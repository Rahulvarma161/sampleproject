import string
import random
import csv
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from .models import users
from django.contrib import messages
from sampleapp.uploadForm import UploadForm
from django.shortcuts import redirect




def uploadfile(request):
   
    if request.method == 'POST':
        exists_email_count = 0
        upload_users_count = 0
        # try:
        with open(request.FILES['excel_file'].temporary_file_path(), 'r') as f:
            book1 = csv.reader(f)
            csv_headings = next(book1)
            column_names = [csv_headings[col_index].lower() for col_index in range(len(csv_headings)) if
                            csv_headings[col_index]]
            # original_column_names = sorted(
            #     ['email', 'name', 'type', 'payment method', 'product', 'date', 'amount', 'order', 'status',
            #      'referrer'])
            # print(column_names)
            original_column_names = sorted(
                ['first name', 'last name', 'date created'])
            check_column_names = sorted(column_names)
            _object_dict_list = []
            if original_column_names != check_column_names:
                return JsonResponse({"error": "Uploaded CSV file columns doesn't match."})
            for row in book1:
                row_data = {key.lower(): value for key, value in zip(csv_headings, row)}
                # print(row_data)
                _object_dict_list.append(row_data)

            for row_index in range(len(_object_dict_list)):
                row_data = _object_dict_list[row_index]
                # print(row_data['email'])
                user_details = users(first_name = row_data['first name'],
                        last_name = row_data['last name'],
                        isactive = 1,
                        create_date=datetime.now(tz=timezone.utc),
                        modified=datetime.now(tz=timezone.utc))
                user_details.save()
        if user_details:
            messages.add_message(
                    request, messages.SUCCESS, 'Users have been uploaded successfully.',
                    fail_silently=True,
                )
        return redirect('uploadfile')
        #return HttpResponse('successfully')
    form = UploadForm()
    return render(request, 'excel.html',{'form': form})
