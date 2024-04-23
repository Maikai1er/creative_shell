from django.shortcuts import render

from cultural_heritage.models import CulturalHeritage


def index(request):
    heritages = CulturalHeritage.objects.all()[:5]
    return render(request, 'index.html', {'heritages': heritages})

