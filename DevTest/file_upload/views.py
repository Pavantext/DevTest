# file_upload/views.py
import pandas as pd
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
from django.utils.html import strip_tags

def upload_file(request):
    summary = None
    table_data = None  # This will hold data for the table

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Read the uploaded file as a DataFrame
                if file.name.endswith('.csv'):
                    df = pd.read_csv(file)
                elif file.name.endswith('.xlsx'):
                    df = pd.read_excel(file)
                else:
                    raise ValueError("Unsupported file format")

                # Rename columns to remove spaces
                df.rename(columns={
                    'Cust State': 'Cust_State',
                    'Cust Pin': 'Cust_Pin',
                    'DPD': 'DPD'
                }, inplace=True)

                # Convert DataFrame to a list of dictionaries
                table_data = df[['Cust_State', 'Cust_Pin', 'DPD']].to_dict('records')

                # Generate a summary as an HTML table
                summary_df = df.describe(include='all')
                summary_html = summary_df.to_html(classes="table table-bordered")

                # Create the email subject dynamically
                user_name = request.user.username if request.user.is_authenticated else "Pavan Kumar M"
                subject = f"Python Assignment - {user_name}"

                # Send email with summary report as an HTML table
                email = EmailMessage(
                    subject=subject,
                    body=summary_html,
                    from_email=settings.EMAIL_HOST_USER,
                    to=['pavantext6@gmail.com'],
                )
                email.content_subtype = "html"  # This is necessary to send HTML email
                email.send(fail_silently=False)

            except Exception as e:
                summary = f"Error processing file: {e}"

    else:
        form = UploadFileForm()

    return render(request, 'file_upload/upload.html', {'form': form, 'summary': summary, 'table_data': table_data})
