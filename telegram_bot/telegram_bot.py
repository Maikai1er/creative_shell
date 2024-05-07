from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
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
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = f'{first_name} {last_name}' if last_name else first_name
    bot.reply_to(message, f'Welcome, {full_name}!')


@bot.message_handler(commands=['stop'])
def stop():
    bot.stop_polling()


def receive_new_heritage(heritage):
    heritage_json = json.dumps(heritage)
    redis_client.set('current_heritage', heritage_json)
    bot.send_message(chat_id='5787733609', text='New object received!')
    bot.send_message(chat_id='5787733609', text=str(heritage))
    bot.send_message(chat_id='5787733609', text='Choose an action:', reply_markup=create_keyboard(['approve', 'reject']))


@bot.message_handler(func=lambda message: message.text in ['approve', 'reject', '/approve', '/reject'])
def handle_decision(message):
    try:
        heritage_json = redis_client.get('current_heritage')
        heritage = json.loads(heritage_json)

        if message.text == '/approve' or message.text == 'approve':
            # Yes, we have to import this here, otherwise server wouldn't start. Hala Django!
            from cultural_heritage.save_object_to_database import save_object_to_database
            save_object_to_database(heritage)
            bot.send_message(message.chat.id, 'Heritage successfully saved to database!')
        if message.text == '/reject' or message.text == 'reject':
            bot.send_message(message.chat.id, 'Heritage is rejected and will not be saved to database!')

        redis_client.delete('current_heritage')
    except TypeError:
        bot.send_message(message.chat.id, 'TypeError, most likely, there is no current heritage to moderate.')


def create_keyboard(buttons):
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for button in buttons:
        keyboard.add(KeyboardButton(text=button))
    return keyboard


@bot.message_handler(func=lambda message: True)
def default_reply(message):
    bot.reply_to(message, text='I don\'t understand, please go talk to ChatGPT <3.')


def send_notification(text):
    bot.send_message(chat_id='5787733609', text=text)


def run_telebot():
    print('Starting telebot ...')
    bot.polling()
