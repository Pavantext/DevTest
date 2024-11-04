# DevTest - Django File Upload and Summary Report
### Overview
The DevTest project is a Django-based web application designed for uploading Excel/CSV files, generating a summary report from the uploaded data, and sending the summary via email. This project demonstrates skills in Django development, file handling, data processing, email functionality, Git, and deployment.

### Features
- File Upload: A user-friendly web interface for uploading Excel/CSV files.
- Data Processing: Reads and summarizes the contents of the uploaded file.
- Email Functionality: Sends the summary report as an email body to a specified email address.
- Deployment: The project is deployed on PythonAnywhere for public access.
### Technologies Used
- Django: For the web application framework
- Pandas: For reading and summarizing the uploaded file
- SMTP: For email functionality
- Git: For version control
- Python Anywhere: For deployment
### Approach
- File Upload: A form in the web interface accepts Excel or CSV files. Files are validated and stored temporarily for processing.
- Data Processing: Using Pandas, the data from the file is processed to create a summary report, similar to the provided sample output.
- Email Summary: Once processed, the summary is emailed to tech@themedius.ai using Django’s SMTP configuration.
- Deployment: The project is deployed on Python Anywhere for easy access and testing.
### Project Structure
- uploader/: Contains the core app files including views, forms, and templates.
- templates/uploader/upload.html: Template for the upload page.
- views.py: Contains the main view logic for file upload, processing, and email sending.
### How to Access
- Live URL: https://paavantext.pythonanywhere.com/
- Visit the link and follow the instructions to upload an Excel or CSV file.
- Upon successful upload and processing, a success message will be displayed, and the summary report will be sent to the specified email.
Repository Link
- GitHub Repository: https://github.com/Pavantext/DevTest
- Configuration
For email functionality, ensure that EMAIL_HOST_USER and EMAIL_HOST_PASSWORD are configured correctly in PythonAnywhere’s environment variables.

