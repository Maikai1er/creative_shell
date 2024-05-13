from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
import redis

TOKEN = '6962411316:AAHb_QYx3XU-JNib6gkhDhOXKEBiW_k6s74'
bot = TeleBot(TOKEN)

redis_host = 'redis'
redis_port = 6379
redis_db = 0
redis_password = 'r3NVuM4N'
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)


# To start moderating, use the '/start' command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = f'{first_name} {last_name}' if last_name else first_name
    bot.reply_to(message, f'Welcome, {full_name}!')
    send_next_heritage()


@bot.message_handler(commands=['stop'])
def stop():
    bot.stop_polling()


def send_next_heritage():
    heritage_json = redis_client.lindex('current_heritage', 0)
    if heritage_json:
        heritage = json.loads(heritage_json)
        heritage_text = (f'Name: {heritage["name"]}.\n'
                         f'Location: {heritage["location"]}.\n'
                         f'Year WHS: {heritage["year_whs"]}.\n'
                         f'Year Endangered: {heritage["year_endangered"]}.\n')
        bot.send_message(chat_id='5787733609', text='New object received!')
        bot.send_message(chat_id='5787733609', text=heritage_text)
        bot.send_message(chat_id='5787733609', text='Choose an action:', reply_markup=create_keyboard(['approve', 'reject']))
    else:
        bot.send_message(chat_id='5787733609', text='No pending objects.')


def push_heritages_to_redis(heritages):
    for heritage in heritages:
        heritage_json = json.dumps(heritage)
        redis_client.rpush('current_heritage', heritage_json)


@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, text='This is a test command to try out the bot functionality!')
    test_heritage = {
        'name': 'test_name',
        'location': 'test_location',
        'year_endangered': 2000,
        'year_whs': 2024,
    }
    push_heritages_to_redis([test_heritage])


@bot.message_handler(func=lambda message: message.text in ['approve', 'reject', '/approve', '/reject'])
def handle_decision(message):
    try:
        heritage_json = redis_client.lpop('current_heritage')
        if heritage_json:
            heritage = json.loads(heritage_json)
            if message.text == '/approve' or message.text == 'approve':
                # Yes, we have to import this here, otherwise server wouldn't start. Hala Django!
                from cultural_heritage.save_object_to_database import save_object_to_database
                save_object_to_database(heritage)
                bot.send_message(message.chat.id, 'Heritage has been successfully saved to database!')
            elif message.text == '/reject' or message.text == 'reject':
                bot.send_message(message.chat.id, 'Heritage is rejected and will not be saved to database!')
            # After moderating a heritage, send the next one
            send_next_heritage()
        else:
            bot.send_message(message.chat.id, 'No pending objects to moderate.')
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


run_telebot()
