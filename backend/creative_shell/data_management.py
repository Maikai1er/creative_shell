from cultural_heritage.models import CulturalHeritage, ContactData
from parser.models import ParsedData


def save_to_heritage_table(heritage_to_save: dict) -> None:

    cultural_heritage = CulturalHeritage(
        name=heritage_to_save.get('name', 'default name'),
        location=heritage_to_save.get('location', 'Location Not Found'),
        year=heritage_to_save.get('year', 0000),
        description=heritage_to_save.get('description', ''),
        category=heritage_to_save.get('category', ''),
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


def save_to_contact_data_table(contact_to_save: dict) -> None:
    # Contact Data model is in cultural_heritage because i'm lazy
    contact_data = ContactData.objects.create(
        name=contact_to_save.get('name', 'default name'),
        contacts=contact_to_save.get('contact', 'Contact Not Found'),
        about=contact_to_save.get('about', 'About Field is Empty'),
    )
    contact_data.save()
