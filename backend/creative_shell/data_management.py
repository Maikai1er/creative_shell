from django.core.exceptions import ValidationError

from cultural_heritage.models import CulturalHeritage, ContactData
from parser.models import ParsedData


def save_to_heritage_table(heritage_to_save: dict) -> None:
    required_fields = ['name', 'location']
    for field in required_fields:
        if not heritage_to_save.get(field):
            raise ValidationError(f'{field} is required')

    cultural_heritage = CulturalHeritage(
        name=heritage_to_save.get('name'),
        location=heritage_to_save.get('location'),
        year=heritage_to_save.get('year', ''),
        reason=heritage_to_save.get('reason', ''),
        image_path=heritage_to_save.get('image_path', '')
    )

    try:
        cultural_heritage.full_clean()
        cultural_heritage.save()
    except ValidationError as e:
        raise ValidationError(e)


def save_to_parsed_table(heritage_to_save: dict) -> None:
    required_fields = ['name', 'location']
    for field in required_fields:
        if not heritage_to_save.get(field):
            raise ValidationError(f'{field} is required for {heritage_to_save.get('name')}')

    parsed_data = ParsedData.objects.create(
        name=heritage_to_save.get('name'),
        location=heritage_to_save.get('location'),
        year=heritage_to_save.get('year', ''),
        reason=heritage_to_save.get('reason', ''),
        image_path=heritage_to_save.get('image_path', '')
    )

    try:
        parsed_data.full_clean()
        parsed_data.save()
    except ValidationError as e:
        raise e


def save_to_contact_data_table(contact_to_save: dict) -> None:
    # Contact Data model is in cultural_heritage because i'm lazy
    required_fields = ['name', 'contacts']
    for field in required_fields:
        if not contact_to_save.get(field):
            raise ValidationError(f'{field} is required')

    contact_data = ContactData.objects.create(
        name=contact_to_save.get('name'),
        contacts=contact_to_save.get('contacts'),
        about=contact_to_save.get('about', ''),
    )

    try:
        contact_data.full_clean()
        contact_data.save()
    except ValidationError as e:
        raise e

