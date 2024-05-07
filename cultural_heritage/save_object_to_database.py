from cultural_heritage.models import CulturalHeritage


def save_object_to_database(object_to_save):

    cultural_heritage = CulturalHeritage(
        name=object_to_save.get('name', 'default name'),
        location=object_to_save.get('location', 'Location Not Found'),
        year_whs=object_to_save.get('Year (WHS)', 0000),
        year_endangered=object_to_save.get('Year (Endangered)', 0000)
    )
    cultural_heritage.save()
