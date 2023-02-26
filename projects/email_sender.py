from email.message import EmailMessage
import ssl
import smtplib

from config import EMAIL_SENDER, EMAIL_APP_PASSWORD, TEMP_EMAIL_RECEIVER

email_sender = EMAIL_SENDER
email_app_password = EMAIL_APP_PASSWORD
email_receiver = TEMP_EMAIL_RECEIVER

subject = "Just a test email sender"
body = """
If you receive this, then you're lucky
"""

em = EmailMessage()
em['From'] = EMAIL_SENDER
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_app_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
