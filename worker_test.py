from telegram_bot.tasks import start_telegram_bot
print('before command')
result = start_telegram_bot.delay()
print('after command')
print(result)
