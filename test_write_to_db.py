from telegram_bot.telegram_bot import receive_new_object

test_heritage = {
    'name': 'test_name',
    'location': 'test_location',
    'year_endangered': 'test_year_endangered',
    'year_whs': 'test_year_whs',
}

receive_new_object(test_heritage)
