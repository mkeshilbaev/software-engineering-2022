import requests
import smtplib

from django.conf import settings


def create_user_service(data):
    print(data)
    try:
        res = requests.post(url='http://user:8000/user/', data=data)
        print(res.json())
        return True
    except Exception as e:
        print(e)
        return False


def send_mail(receivers, email, subject):
    sender = settings.EMAIL_HOST_USER
    receivers = receivers
    password = settings.EMAIL_HOST_PASSWORD
    subject = subject
    text = email
    message = 'Subject: {}\n\n{}'.format(subject, text)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, password)
        server.sendmail(
            sender,
            receivers,
            message
        )
        server.quit()
        return 'ok'
    except smtplib.SMTPException:
        print("Error: unable to send email")
        return 'error'

