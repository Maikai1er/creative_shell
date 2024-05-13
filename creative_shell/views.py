from django.http import JsonResponse
from django.db.models.functions import Random

from cultural_heritage.models import CulturalHeritage


def load_more_heritages(request):

    heritages = CulturalHeritage.objects.all().order_by(Random())[:5]

    data = [{
        'name': heritage.name,
        'location': heritage.location,
        'year_whs': heritage.year_whs,
        'year_endangered': heritage.year_endangered
    } for heritage in heritages]

    return JsonResponse(data, safe=False)


def index(request):
    heritages = CulturalHeritage.objects.all().order_by(Random())[:5]

    data = [{
        'name': heritage.name,
        'location': heritage.location,
        'year_whs': heritage.year_whs,
        'year_endangered': heritage.year_endangered
    } for heritage in heritages]

    return JsonResponse(data, safe=False)
