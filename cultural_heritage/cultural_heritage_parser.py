import requests
from bs4 import BeautifulSoup

# returns heritages list in format:
# [{'name': 'Abu Mena', 'location': 'Abusir'},
# {'name': 'Air and Ténéré Natural Reserves', 'location': 'Arlit Department'},
# {'name': 'Ancient City of Aleppo', 'location': 'Aleppo Governorate'}.... ]


def cultural_heritage_parser():
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
        if cells:
            second_cell = cells[1]
            link = second_cell.find('a', href=True, title=True)
            if link:
                text = link.get_text(strip=True)
                heritage['location'] = text
        heritages.append(heritage)
    return heritages
