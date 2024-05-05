from creative_shell.celery import app
from .telegram_bot import run_telebot


@app.task
def start_telegram_bot():
    print('RUN OVER HERE')
    run_telebot()
