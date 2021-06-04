import os
import smtplib

from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv('.env')

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


class Mailer:
    def __init__(self, subject, sender_email, sender_name, content):
        self.msg = EmailMessage()
        self.msg['Subject'] = subject
        self.msg['From'] = sender_email
        self.msg['to'] = EMAIL_ADDRESS
        self.msg.set_content("This message is from: {email} \n\n {content} \n\n Kind regards, \n\n {name}"
                             .format(email=sender_email, content=content, name=sender_name))

    def send(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(self.msg)

