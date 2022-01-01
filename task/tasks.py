
from celery.celery import app
from django.core.mail import send_mail

from .models import Contact
from .service import send

@app.task
def send_spam_email(user_email):
    send(user_email)

@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            [contact.email],
            fail_silintly=false
        )