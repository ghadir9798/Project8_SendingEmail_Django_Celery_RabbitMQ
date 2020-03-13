from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep 
from django.core.mail import send_mail


# This function is just for testing purposes
@shared_task
def sleepy(duration):
    sleep(duration)
    return None

# Main Function
@shared_task
def send_email_task():
    sleep(10)
    send_mail(
        'Celery Task has been Worked!',
        'This is the proof that celery task has been worked correctly',
        'YOUR GMAIL ADDRESS',
        ['OTHER EMAIL ADDRESSES to send email to them'],
        fail_silently=False,
    )
    return 'The Email has been delivered successfully'