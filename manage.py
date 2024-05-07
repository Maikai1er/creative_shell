#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading

from telegram_bot.telegram_bot import run_telebot


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fuck_celery.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if not os.environ.get('TELEBOT_ALREADY_RUNNING'):
        os.environ['TELEBOT_ALREADY_RUNNING'] = 'True'
        bot_thread = threading.Thread(target=run_telebot)
        bot_thread.start()

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
