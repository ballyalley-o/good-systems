import os
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from logic.constants.constants import *
from dotenv import load_dotenv
load_dotenv()

def send_email(subject, body, to_email, attachment_path, name):
    # Email configuration
    sender_email = os.getenv('SMTP_SENDER')
    sender_password = os.getenv('SMTP_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')

    # Create the email message
    message = MIMEMultipart()
    message["From"] = "Institute of Data"
    message["To"] = to_email
    cc_emails = os.getenv('SMTP_CC_TEST').split(';')
    # cc_emails = os.getenv('CC_EMAIL')
    if cc_emails:
        message["Cc"] = ', '.join(cc_emails)
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    # Attach the file if provided
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            filename=os.path.basename(attachment_path)
            part = MIMEApplication(attachment.read(), Name=filename)
            part['Content-Disposition'] = f'attachment; filename="{filename}"'
            message.attach(part)

    # Establish a secure connection to the SMTP server
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        # Login to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, [to_email] + cc_emails, message.as_string())

    print(f"Email with attachment sent successfully to {to_email}")

# Example usage for 16 students with individual attachments
subject = EMAIL_SUBJECT

# TODO: put in .env file
students_attachments = json.loads(os.getenv('SMTP_ATTACHMENTS_TEST'))


# Send emails to each student with their individual attachment
for student_email, (attachment_path, name) in students_attachments.items():
    body = f"Hi {name},\n\nAttached is your Progress Report to date, please find it for your review."
    send_email(subject, body, student_email, attachment_path, name)



# TODO: html body instead of plain text.