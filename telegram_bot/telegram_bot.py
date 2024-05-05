from telebot import TeleBot


TOKEN = '6962411316:AAHb_QYx3XU-JNib6gkhDhOXKEBiW_k6s74'
bot = TeleBot(TOKEN)

# chat_id=5787733609


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')


@bot.message_handler(commands=['run'])
def start_bot():
    bot.polling()


@bot.message_handler(commands=['stop'])
def stop():
    bot.stop_polling()


def send_notification(text):
    bot.send_message(chat_id='5787733609', text=text)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


def run_telebot():
    print('Starting telebot ...')
    bot.polling()


# что по большому счету нужно
# 1. бот здоровается
# 2. бот запускается на сервере и сидит запущенным
# 3. один раз в какое-то время (допустим, день), запускается программа по поиску новых ОКН
# 4. после этого нам нужна валидация полученной информации
# 5. после валидации полученная информация разбивается на куски (объекты) и по одному передается
# в функцию в боте, которая превратит сырую информацию в удобоваримую для пользователя
# 6. После этого, бот посылает в чат сообщение о том, что был найден новый объект (1 сообщение для 1 объекта)
# 7. И нам нужно в целом 2 кнопки (пока 2). Первая - апрувнуть объект. Вторая - отклонить объект
# 8. Если объект апрувнут - информация передается дальше в функцию, которая запишет его в БД
# 9. Если объект отклонен - информация уничтожается
