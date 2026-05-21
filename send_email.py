import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

GMAIL_ADDRESS = os.environ["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

def send_email():
    recipient = "kmadhav03@gmail.com"  # change this
    subject = "Your Daily Email"
    body = "Hello! This is your scheduled email."

    msg = MIMEMultipart()
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_ADDRESS, recipient, msg.as_string())
        print("Email sent successfully!")

    print(f"Script ran at: {datetime.datetime.utcnow()} UTC")

if __name__ == "__main__":
    send_email()