from celery import shared_task
from .utils import send_mail


@shared_task
def send_notification(subject, email, receivers):
    res = send_mail(receivers=receivers, email=email, subject=subject)
    print(res)


@shared_task
def sum(a, b):
    return a + b
