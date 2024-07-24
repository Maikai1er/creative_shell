import os
import requests
from bs4 import BeautifulSoup
from cultural_heritage.models import CulturalHeritage
from creative_shell.data_management import save_to_parsed_table

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'
}


def download_image(img_url, save_path):
    try:
        img_response = requests.get(img_url, headers=HEADERS, stream=True)
        img_response.raise_for_status()
        with open(save_path, 'wb') as file:
            for chunk in img_response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'Image downloaded: {save_path}')
    except requests.RequestException as e:
        print(f'Error downloading image {img_url}: {e}')


def get_image_url(cell):
    img_tag = cell.find('img')
    if img_tag and 'src' in img_tag.attrs:
        img_url = img_tag['src']
        img_url = requests.compat.urljoin('https://upload.wikimedia.org', img_url)
        return img_url
    return None


def parse_wiki(url) -> list:
    response = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.find(class_='wikitable plainrowheaders sortable')
    rows = table.find_all('tr')

    heritages = []
    for row in rows:
        heritage = {}
        cells = row.find_all('td')
        if len(cells) < 8:
            continue

        name_cell = row.find('th')
        if name_cell:
            heritage['name'] = name_cell.get_text(strip=True)

        location_cell = cells[1]
        link = location_cell.find('a', href=True, title=True)
        if link:
            heritage['location'] = link.get_text(strip=True)

        img_tag = cells[0].find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
            img_url = requests.compat.urljoin('https://upload.wikimedia.org', img_url)

        if img_url:
            img_filename = f"{heritage['name'].replace('/', '_').replace(':', '_')}.jpg"
            img_path = os.path.join('/app/shared/images/', img_filename)
            download_image(img_url, img_path)
            heritage['image_path'] = img_filename

        year_cell = cells[5]
        if year_cell:
            heritage['year'] = year_cell.get_text(strip=True)

        reason_cell = cells[6]
        if reason_cell:
            heritage['reason'] = reason_cell.get_text(strip=True)

        heritages.append(heritage)

    return heritages


def parse_and_save_to_temp_table() -> None:
    url = 'https://en.wikipedia.org/wiki/List_of_World_Heritage_in_Danger'
    heritages = parse_wiki(url)

    for heritage in heritages:
        if not CulturalHeritage.objects.filter(name=heritage['name']).exists():
            save_to_parsed_table(heritage)
