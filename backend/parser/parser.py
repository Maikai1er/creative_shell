from cultural_heritage.models import CulturalHeritage
import requests
from bs4 import BeautifulSoup
from creative_shell.data_management import save_to_parsed_table


# WARNING: THIS IS ONLY A TEST PARSER !!!
# SECOND WARNING: THIS IS AN OMEGA TEST PARSER!!!!!!


def parse_wiki(url) -> list:
    response = requests.get(url, headers=None).text
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.find(class_='wikitable plainrowheaders sortable')
    rows = table.find_all('tr')
    heritages = []
    for row in rows:
        heritage = {}
        name = row.find('th')
        if name.text.strip('\n') == 'Name':
            continue

        heritage['name'] = name.text.strip('\n')
        cells = row.find_all('td')
        location_cell = cells[1]
        link = location_cell.find('a', href=True, title=True)
        if link:
            location_text = link.get_text(strip=True)
            heritage['location'] = location_text

        year_endangered_cell = cells[5]
        if year_endangered_cell:
            year_endangered_text = year_endangered_cell.get_text(strip=True)
            heritage['year_endangered'] = year_endangered_text

        reason_cell = cells[6]
        if reason_cell:
            reason_text = reason_cell.get_text(strip=True)
            heritage['reason'] = reason_text

        heritages.append(heritage)
    return heritages


def parse_and_save_to_temp_table() -> None:
    url = 'https://en.wikipedia.org/wiki/List_of_World_Heritage_in_Danger'
    heritages = parse_wiki(url)

    for heritage in heritages:
        if not CulturalHeritage.objects.filter(name=heritage['name']).exists():
            save_to_parsed_table(heritage)
