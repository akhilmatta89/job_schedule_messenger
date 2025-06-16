import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_SUBJECT = "NEW TIME SHEET RELEASED"


class TriggerJob:

    def send_message(self, df):
        for index, row in df.iterrows():
            try:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = row[2]
                msg['Subject'] = EMAIL_SUBJECT

                msg.attach(MIMEText(f"Hi {row[0]} your rooster for today is scheduled and time alloted is {row[3]}", 'plain'))

                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    server.sendmail(EMAIL_ADDRESS, row[2], msg.as_string())

                print("Email sent Succesfully")
            except Exception as e:
                print(f"Error sending mail: {e}")
