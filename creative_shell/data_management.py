from cultural_heritage.models import CulturalHeritage
from parser.models import ParsedData


def save_to_heritage_table(heritage_to_save: dict) -> None:

    cultural_heritage = CulturalHeritage(
        name=heritage_to_save.get('name', 'default name'),
        location=heritage_to_save.get('location', 'Location Not Found'),
        year_whs=heritage_to_save.get('Year (WHS)', 0000),
        year_endangered=heritage_to_save.get('Year (Endangered)', 0000)
    )
    cultural_heritage.save()


def save_to_parsed_table(heritage_to_save: dict) -> None:
    parsed_data = ParsedData.objects.create(
        name=heritage_to_save.get('name', 'default name'),
        location=heritage_to_save.get('location', 'Location Not Found'),
        year_whs=heritage_to_save.get('Year (WHS)', 0000),
        year_endangered=heritage_to_save.get('Year (Endangered)', 0000)
    )
    parsed_data.save()
