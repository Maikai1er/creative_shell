import json

from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import redis

TOKEN = '6962411316:AAHb_QYx3XU-JNib6gkhDhOXKEBiW_k6s74'
bot = TeleBot(TOKEN)

redis_host = 'localhost'
redis_port = 6379
redis_db = 0
redis_password = 'r3NVuM4N'
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)
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


def receive_new_object(heritage):
    heritage_json = json.dumps(heritage)
    redis_client.set('current_heritage', heritage_json)
    bot.send_message(chat_id='5787733609', text='New object received!')
    bot.send_message(chat_id='5787733609', text=str(heritage))
    bot.send_message(chat_id='5787733609', text='Choose an action:', reply_markup=create_keyboard(['approve', 'reject']))


@bot.message_handler(func=lambda message: message.text in ['approve', 'reject'])
def handle_decision(message):
    try:
        heritage_json = redis_client.get('current_heritage')
        print(heritage_json)
        heritage = json.loads(heritage_json)
        if not heritage_json:
            bot.send_message(message.chat.id, 'Error: No current heritage')
            return

        if message.text == 'approve':
            from cultural_heritage.save_object_to_database import save_object_to_database
            save_object_to_database(heritage)
            bot.send_message(message.chat.id, 'Heritage successfully saved to database!')
        elif message.text == 'reject':
            bot.send_message(message.chat.id, 'Heritage is rejected and will not be saved to database!')

        redis_client.delete('current_heritage')
    except Exception as e:
        bot.send_message(message.chat.id, 'Error: ' + str(e))


def create_keyboard(buttons):
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for button in buttons:
        keyboard.add(KeyboardButton(text=button))
    return keyboard


def send_notification(text):
    bot.send_message(chat_id='5787733609', text=text)


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
