import smtplib
import os
from twilio.rest import Client

account_sid = os.environ['Account_SID']
auth_token = os.environ['Auth_Token']
MAIL_PROVIDER_SMTP_ADRESS = "smtp.gmail.com"
MY_EMAIL = os.environ['EMAIL']
MY_PASSWORD = os.environ['PASSWORD']

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)
    def send_sms(self,message):
        message= self.client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',
            to='whatsapp:+905343295012'
    )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight! \n\n{message}\n{google_flight_link}".encode('utf-8')
                )