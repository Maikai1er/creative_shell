from telegram_bot.tasks import start_telegram_bot

start_telegram_bot.delay()
#
# from telegram_bot.run_telebot import bot
#
# bot.send_message(chat_id='5787733609', text='/run')
