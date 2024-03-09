import os
import smtplib
import json
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from logic.constants.constants import *
from logic.constants.html import html_template
from dotenv import load_dotenv
load_dotenv()

def send_email(subject, body, to_email, attachment_path, name):
    """
    Sends an smtp email with an optional attachment for students report card.

    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        to_email (str): The recipient's email address.
        attachment_path (str): The file path of the attachment (optional).
        name (str): The name of the sender.

    Returns:
        None
    """
    sender_email = os.getenv('SMTP_SENDER')
    sender_password = os.getenv('SMTP_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')

    message = MIMEMultipart()
    message["From"] = "Institute of Data"
    message["To"] = to_email
    cc_emails = os.getenv('SMTP_CC_TEST').split(';')

    if cc_emails:
        message["Cc"] = ', '.join(cc_emails)
    message["Subject"] = subject

    message.attach(MIMEText(body, "html"))

    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            filename=os.path.basename(attachment_path)
            part = MIMEApplication(attachment.read(), Name=filename)
            part['Content-Disposition'] = f'attachment; filename="{filename}"'
            message.attach(part)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [to_email] + cc_emails, message.as_string())

    print(f"{EMAIL_SENT.format(to_email)}")


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
