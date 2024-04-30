import os

import django
import requests
from bs4 import BeautifulSoup
import re

from telegram_bot.run_telebot import send_notification

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creative_shell.settings')

django.setup()

from cultural_heritage.save_object_to_database import save_object_to_database


# returns heritages list in format:
# [{'name': 'Abu Mena', 'location': 'Abusir'},
# {'name': 'Air and Ténéré Natural Reserves', 'location': 'Arlit Department'},
# {'name': 'Ancient City of Aleppo', 'location': 'Aleppo Governorate'}.... ]
# WARNING: THIS IS ONLY A TEST PARSER !!!
# SECOND WARNING: THIS IS AN OMEGA TEST PARSER!!!!!!


def parse_wiki():
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) '
    #                   'Chrome/80.0.3987.162 Safari/537.36',
    #     'Accept-Language': 'en-US,en;q=0.9',
    # }
    url = 'https://en.wikipedia.org/wiki/List_of_World_Heritage_in_Danger'
    response = requests.get(url, headers=None).text
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.find(class_='wikitable plainrowheaders sortable')
    # 'wikitable plainrowheaders sortable jquery-tablesorter'
    rows = table.find_all('tr')
    heritages = []
    for row in rows:
        heritage = {}
        name = row.find('th')
        if name.text.strip('\n') == 'Name':
            continue
        heritage['name'] = name.text.strip('\n')

        cells = row.find_all('td')

        pattern = re.compile(r'\d+')
        years = []
        for td in cells:
            td_text = td.get_text(strip=True)

            numbers = pattern.findall(td_text)
            filtered_numbers = filter(lambda x: len(x) == 4, numbers)
            for number in filtered_numbers:
                years.append(int(number))
                heritage['Year (WHS)'] = years[0]
                if len(years) > 1:
                    heritage['Year (Endangered)'] = years[1]
        #     br = td.find_all('br')
        #     print(br)
        # #     print(td)
        # #     span_elements = td.find_all('br')
        # #     for span_element in span_elements:
        # #         print(span_element)
        # #         # text = span_element.get_text(strip=True)
        # #         # print(text)
        if cells:
            second_cell = cells[1]
            link = second_cell.find('a', href=True, title=True)
            if link:
                text = link.get_text(strip=True)
                heritage['location'] = text
        heritages.append(heritage)
    return heritages


def save_to_database():
    heritages = parse_wiki()

    send_notification('parser started')

    for heritage in heritages:
        save_object_to_database(heritage)


save_to_database()
