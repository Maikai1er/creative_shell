import os
import re

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
        if isinstance(location_cell, str):
            soup = BeautifulSoup(location_cell, 'html.parser')
        else:
            soup = location_cell

        for elem in soup.select('.geo-inline, .geo'):
            elem.decompose()

        for elem in soup.select('[style*="display: none"]'):
            elem.decompose()

        cell_text = soup.get_text(separator=' ', strip=True)

        country_match = re.search(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b', cell_text)
        country = country_match.group(1) if country_match else None

        region_matches = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*)\b', cell_text)
        regions = [match for match in region_matches if match != country]

        place_links = soup.find_all('a')
        place_names = [link.get_text() for link in place_links if link.get_text() not in (country, *regions)]

        if not country:
            flag_span = soup.find('span', class_='flagicon')
            if flag_span and flag_span.find_next_sibling(text=True):
                country = flag_span.find_next_sibling(text=True).strip()

        regions = list(dict.fromkeys(filter(None, regions)))
        place_names = list(dict.fromkeys(filter(None, place_names)))

        location_parts = []
        if country:
            location_parts.append(country)
        if regions:
            location_parts.append(', '.join(regions))
        if place_names:
            location_parts.append(', '.join(place_names))

        location_string = ' - '.join(location_parts)

        heritage['location'] = location_string

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
