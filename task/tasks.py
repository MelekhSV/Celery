import shared as shared
from send_mail.celery import app
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
            "Вы подписались на рассылку",
            "Мы будет писатиь много спасма каждые 5 мин",
            "melesergey74@gmail.com",
            [contact.email],
            fail_silently=False,
        )


@app.task
def my_task(a, b):
    c = a + b
    return c


@app.task
def my_task_as(d, e):
    c = d + e
    return c


@app.task(bind=True, default_retry_delay=5 * 60)
def my_task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@shared.task()
def my_sh_task(msg):
    return msg + "!!!"
