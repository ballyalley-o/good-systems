import os
import csv
import sys
from logic.constants.constants import *
from logic.constants.html import html_template
from logic.smtp_send_email import send_email
from dotenv import load_dotenv
load_dotenv()

attachment_abs_path_template = os.getenv('SMTP_ATTACHMENT_ABSOLUTE_PATH')

specific_student_name = sys.argv[1].capitalize()

with open(os.getenv('SMTP_STUDENT_INFO_TEST'), 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Firstname']
        if specific_student_name == name:
            student_email = row['Email']
            attachment_abs_path = attachment_abs_path_template.replace('{student_name}', name)
            attachment_path = attachment_abs_path

            if len(sys.argv) > 2:
                if sys.argv[2] == '-u':
                    body = html_template.format(header=os.getenv('SMTP_EMAIL_HEADER'), name=name, emailContent=EMAIL_CONTENT_UPDATE, company=COMPANY_NAME)
                    send_email(EMAIL_SUBJECT_UPDATE, body, student_email, attachment_path, name)
            else:
                body = html_template.format(header=os.getenv('SMTP_EMAIL_HEADER'), name=name, emailContent=EMAIL_CONTENT, company=COMPANY_NAME)
                send_email(EMAIL_SUBJECT, body, student_email, attachment_path, name)