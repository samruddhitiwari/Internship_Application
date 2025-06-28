from celery import shared_task
import time

@shared_task
def send_welcome_email(username):
    print(f"📨 Sending welcome email to {username}...")
    time.sleep(5)
    print(f"✅ Welcome email sent to {username}!")
    return f"Email sent to {username}"
from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username or self.telegram_id
