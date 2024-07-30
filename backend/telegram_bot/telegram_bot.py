import os

import requests
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv('TOKEN')
bot = TeleBot(TOKEN)


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


def get_next_heritage():
    response = requests.get('http://192.168.1.36:8000/get_next_heritage/')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def send_next_heritage() -> None:
    try:
        heritage = get_next_heritage()
        heritage_text = (f'Name: {heritage['name']}.\n'
                         f'Location: {heritage['location']}.\n'
                         f'Year: {heritage['year']}.\n'
                         f'Reason: {heritage['reason']}.')
        bot.send_message(chat_id='5787733609', text='New object received!')
        bot.send_message(chat_id='5787733609', text=heritage_text)
        image_path = f'/app/shared/images/{heritage['name']}.jpg'
        if os.path.exists(image_path):
            with open(image_path, 'rb') as photo:
                bot.send_photo(chat_id='5787733609', photo=photo)
        else:
            bot.send_message(chat_id='5787733609', text='Image not found!')
        bot.send_message(chat_id='5787733609', text='Choose an action:', reply_markup=create_keyboard(['approve', 'reject']))
    except Exception:
        bot.send_message(chat_id='5787733609', text='Error sending next heritage!')


def save_heritage(heritage_data, decision):
    url = 'http://192.168.1.36:8000/save_heritage/'
    payload = {'data': heritage_data, 'decision': decision}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        bot.send_message(chat_id='5787733609', text='Successfully executed!')
    else:
        bot.send_message(chat_id='5787733609', text=f'Failed to save heritage:, {response.status_code}.\n'
                                                    f'{response.text}.\n'
                                                    f'{payload}.')


@bot.message_handler(func=lambda message: message.text in ['approve', 'reject', '/approve', '/reject'])
def handle_decision(message):
    try:
        heritage = get_next_heritage()
        if heritage:
            if message.text == '/approve' or message.text == 'approve':
                save_heritage(heritage, decision='approve')
            elif message.text == '/reject' or message.text == 'reject':
                save_heritage(heritage, decision='reject')
            send_next_heritage()
        else:
            bot.send_message(message.chat.id, 'No pending objects to moderate.')
    except Exception as e:
        bot.send_message(message.chat.id, f'Failed to moderate heritage: {e}')


def create_keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
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
