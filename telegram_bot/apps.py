# from django.apps import AppConfig
# from django.db.models.signals import post_migrate
# from django.core.signals import request_finished, request_started
# from django.dispatch import receiver
# from telegram_bot.run_telebot import bot
#
#
# class TelegramBotConfig(AppConfig):
#     name = 'telegram_bot'
#
#     def ready(self):
#         print('before migration...')
#         post_migrate.connect(self.start_telebot)
#         print('before request start...')
#         request_started.connect(self.stop_telebot)
#         print('before request finished...')
#         request_finished.connect(self.stop_telebot)
#
#     def start_telebot(self, **kwargs):
#         print('before telebot start...')
#         bot.polling()
#
#     def stop_telebot(self, **kwargs):
#         print('before telebot stop...')
#         bot.stop_polling()
