import os
import smtplib

from dotenv import load_dotenv
from email.message import EmailMessage


class Mailer:
    def __init__(self, subject, sender_email, sender_name, content):
        load_dotenv()
        self.email = os.environ.get('EMAIL_USER')
        self.password = os.environ.get('EMAIL_PASSWORD')
        self.msg = EmailMessage()
        self.msg['Subject'] = subject
        self.msg['From'] = sender_email
        self.msg['to'] = self.email
        self.msg.set_content("This message is from: {email} \n\n {content} \n\n Kind regards, \n\n {name}"
                             .format(email=sender_email, content=content, name=sender_name))

    def send(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.email, self.password)

            smtp.send_message(self.msg)
