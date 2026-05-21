import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
from dotenv import load_dotenv

load_dotenv()
GMAIL_ADDRESS = os.environ["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

def send_email():
    recipients = [
        "kmadhav03@gmail.com",
        "dearvenumadhav@gmail.com"
    ]
    subject = "Your Daily Email"
    body = "Hello! This is your scheduled email."

    msg = MIMEMultipart()
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_ADDRESS, recipients, msg.as_string())
        print("Email sent successfully!")

    print(f"Script ran at: {datetime.datetime.now(datetime.UTC)} UTC")

if __name__ == "__main__":
    send_email()