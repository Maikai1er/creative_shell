# from django.apps import AppConfig
# from django.db.models.signals import post_migrate
# from django.dispatch import receiver
#
#
# class YourAppConfig(AppConfig):
#     name = 'telegram_bot'
#
#     def ready(self):
#         from telegram_bot.run_telebot import run_telebot
#         post_migrate.connect(run_telebot)
