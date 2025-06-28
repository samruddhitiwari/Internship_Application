import telegram
from telegram.ext import Updater, CommandHandler
from django.conf import settings
from core.models import TelegramUser
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJANGO_INTERN_APP.settings")
django.setup()

def start(update, context):
    user = update.effective_user
    TelegramUser.objects.update_or_create(
        telegram_id=user.id,
        defaults={
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    )
    update.message.reply_text(f"👋 Hello {user.first_name}! You’re now registered with the Django Intern App.")

def main():
    updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
