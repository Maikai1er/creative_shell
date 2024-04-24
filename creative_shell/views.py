from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from cultural_heritage.models import CulturalHeritage


def load_more_heritages(request):
    offset = int(request.GET.get('offset', 0))
    limit = 5

    heritages = CulturalHeritage.objects.all()[offset:offset + limit]
    data = [{
        'name': heritage.name,
        'location': heritage.location,
        'year_whs': heritage.year_whs,
        'year_endangered': heritage.year_endangered}
        for heritage in heritages]

    return JsonResponse(data, safe=False)


def index(request):
    heritages = CulturalHeritage.objects.all()  # Получаем первые 5 объектов
    return render(request, 'index.html', {'heritages': heritages})
