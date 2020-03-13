from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from .tasks import sleepy, send_email_task

def index(request):
    # send_email_task()
    # return HttpResponse("<h1>Email has been sent successfully Without using CELERY!</h1>")
    send_email_task.delay()
    return HttpResponse("<h1>Email has been sent successfully With CELERY!</h1>")
