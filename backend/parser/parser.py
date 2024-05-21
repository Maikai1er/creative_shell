import os

from cultural_heritage.models import CulturalHeritage
import requests
from bs4 import BeautifulSoup
from creative_shell.data_management import save_to_parsed_table, save_to_heritage_table
import pandas as pd


# returns heritages list in format:
# [{'name': 'Abu Mena', 'location': 'Abusir'},
# {'name': 'Air and Ténéré Natural Reserves', 'location': 'Arlit Department'},
# {'name': 'Ancient City of Aleppo', 'location': 'Aleppo Governorate'}.... ]
# WARNING: THIS IS ONLY A TEST PARSER !!!
# SECOND WARNING: THIS IS AN OMEGA TEST PARSER!!!!!!


# def parse_wiki(url) -> list:
#     response = requests.get(url, headers=None).text
#     soup = BeautifulSoup(response, 'html.parser')
#     table = soup.find(class_='wikitable plainrowheaders sortable')
#     rows = table.find_all('tr')
#     heritages = []
#     for row in rows:
#         heritage = {}
#         name = row.find('th')
#         if name.text.strip('\n') == 'Name':
#             continue
#
#         heritage['name'] = name.text.strip('\n')
#         cells = row.find_all('td')
#         location_cell = cells[1]
#         link = location_cell.find('a', href=True, title=True)
#         if link:
#             location_text = link.get_text(strip=True)
#             heritage['location'] = location_text
#
#         year_whs_cell = cells[4]
#         if year_whs_cell:
#             year_whs_text = year_whs_cell.get_text(strip=True)
#             heritage['year_whs'] = year_whs_text
#
#         year_endangered_cell = cells[5]
#         if year_endangered_cell:
#             year_endangered_text = year_endangered_cell.get_text(strip=True)
#             heritage['year_endangered'] = year_endangered_text
#
#         reason_cell = cells[6]
#         if reason_cell:
#             reason_text = reason_cell.get_text(strip=True)
#             heritage['reason'] = reason_text
#
#         heritages.append(heritage)
#     return heritages


def parse_xlsx() -> list:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'heritages.xlsx')
    df = pd.read_excel(file_path)
    heritages = []

    for index, row in df.iterrows():
        heritage = {
            'name': row['name_en'],
            'year': row['date_inscribed'],
            'description': row['short_description_en'].replace('<p>', '').replace('</p>', ''),
            'category': row['category'],
            'location': row['states_name_en']
        }
        heritages.append(heritage)
    return heritages


def parse_and_save_to_temp_table() -> None:
    heritages = parse_xlsx()
    for heritage in heritages:
        save_to_heritage_table(heritage)


# def parse_and_save_to_temp_table() -> None:
#     url = 'https://en.wikipedia.org/wiki/List_of_World_Heritage_in_Danger'
#     heritages = parse_wiki(url)
#
#     for heritage in heritages:
#         if not CulturalHeritage.objects.filter(name=heritage['name']).exists():
#             save_to_parsed_table(heritage)
