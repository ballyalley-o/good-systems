import os
import smtplib
import csv
from logic.constants.constants import *
from logic.constants.html import html_template
from logic.smtp_send_email import send_email
from dotenv import load_dotenv
load_dotenv()

subject = EMAIL_SUBJECT
attachment_abs_path_template = os.getenv('SMTP_ATTACHMENT_ABSOLUTE_PATH')

with open(os.getenv('SMTP_STUDENT_INFO'), 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Firstname']
        student_email = row['Email']
        attachment_abs_path = attachment_abs_path_template.replace('{student_name}', name)
        attachment_path = attachment_abs_path
        body = html_template.format(header=os.getenv('SMTP_EMAIL_HEADER'), name=name, emailContent=EMAIL_CONTENT, company=COMPANY_NAME)
        send_email(subject, body, student_email, attachment_path, name)

