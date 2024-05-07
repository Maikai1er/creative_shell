from django.http import JsonResponse
from django.shortcuts import render
from django.db.models.functions import Random

from cultural_heritage.models import CulturalHeritage


def load_more_heritages(request):
    limit = 5

    # Перемешиваем записи и выбираем случайные объекты
    heritages = CulturalHeritage.objects.all().order_by(Random())[:limit]

    data = [{
        'name': heritage.name,
        'location': heritage.location,
        'year_whs': heritage.year_whs,
        'year_endangered': heritage.year_endangered}
        for heritage in heritages]

    return JsonResponse(data, safe=False)


def index(request):
    # Получаем первые 5 случайных объектов для отображения на главной странице
    heritages = CulturalHeritage.objects.all().order_by(Random())[:5]
    return render(request, 'index.html', {'heritages': heritages})
