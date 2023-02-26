from email.message import EmailMessage
import ssl
import smtplib

from config import EMAIL_SENDER, EMAIL_APP_PASSWORD, TEMP_EMAIL_RECEIVER

def send_email(email_sender, email_app_password, email_receiver):

    subject = "Just a test email sender"
    body = """
    If you receive this, then this is your lucky day!
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

if __name__ == "__main__":
    send_email(EMAIL_SENDER, EMAIL_APP_PASSWORD, TEMP_EMAIL_RECEIVER)
