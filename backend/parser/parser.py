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


def parse_wiki(url) -> list:
    response = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.find(class_='wikitable plainrowheaders sortable')
    rows = table.find_all('tr')

    heritages = []
    for row in rows[1:]:
        cells = row.find_all(['th', 'td'])
        if len(cells) < 8:
            continue

        heritage = {}
        heritage['name'] = cells[0].get_text(strip=True)

        location_cell = cells[1]
        for elem in location_cell.select('.geo-inline, .geo, [style*="display: none"]'):
            elem.decompose()

        location_text = location_cell.get_text(separator=' ', strip=True)

        country_match = re.search(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b', location_text)
        country = country_match.group(1) if country_match else None

        if not country:
            flag_span = location_cell.find('span', class_='flagicon')
            if flag_span and flag_span.find_next_sibling(text=True):
                country = flag_span.find_next_sibling(text=True).strip()

        region_matches = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+[A-Z][a-z]+)*)\b', location_text)
        regions = [match for match in region_matches if match != country]

        place_links = location_cell.find_all('a')
        place_names = [link.get_text() for link in place_links if link.get_text() not in (country, *regions)]

        location_parts = [part for part in [country, ', '.join(regions), ', '.join(place_names)] if part]
        heritage['location'] = ' - '.join(location_parts)

        img_tag = cells[0].find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = requests.compat.urljoin('https://upload.wikimedia.org', img_tag['src'])
            img_filename = f"{heritage['name'].replace('/', '_').replace(':', '_')}.jpg"
            img_path = os.path.join('/app/shared/images/', img_filename)
            download_image(img_url, img_path)
            heritage['image_path'] = img_filename

        heritage['year'] = cells[5].get_text(strip=True)
        heritage['reason'] = cells[6].get_text(strip=True)

        heritages.append(heritage)

    return heritages


def parse_and_save_to_temp_table() -> None:
    url = 'https://en.wikipedia.org/wiki/List_of_World_Heritage_in_Danger'
    heritages = parse_wiki(url)

    for heritage in heritages:
        if not CulturalHeritage.objects.filter(name=heritage['name']).exists():
            save_to_parsed_table(heritage)