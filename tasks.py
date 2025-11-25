# tasks.py
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv(dotenv_path="/Users/mainakdey/Documents/GitHub/email-rq/email.env")

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email_task(to_email, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.ehlo()               
            server.starttls()         
            server.ehlo()         
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print("Email sent successfully!")
        return "OK"

    except Exception as e:
        print("FAILED:", e)
        return str(e)
