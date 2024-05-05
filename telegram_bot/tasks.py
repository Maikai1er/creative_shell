from creative_shell.celery import app
from .run_telebot import run_telebot, stop_telebot


@app.task
def start_telegram_bot():
    print('RUN OVER HERE')
    run_telebot()


@app.task
def stop_telegram_bot():
    print('STOP OVER HERE')
    stop_telebot()
