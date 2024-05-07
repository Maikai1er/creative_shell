from telegram_bot.telegram_bot import receive_new_heritage

test_heritage = {
    'name': 'test_name',
    'location': 'test_location',
    'year_endangered': 2000,
    'year_whs': 2024,
}

receive_new_heritage(test_heritage)
