from cultural_heritage.models import CulturalHeritage


def save_object_to_database(object_to_save):
    cultural_heritage = CulturalHeritage(
        name=object_to_save['name'],
        location=object_to_save.get('location', 'Location Not Found'),
        year_whs=object_to_save.get('Year (WHS)', None),
        year_endangered=object_to_save.get('Year (Endangered)', None)
    )
    cultural_heritage.save()
