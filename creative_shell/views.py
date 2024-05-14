import json

from django.http import JsonResponse, HttpResponse
from django.db.models.functions import Random
from django.views.decorators.csrf import csrf_exempt

from cultural_heritage.models import CulturalHeritage
from parser.models import ParsedData
from parser.parser import pass_to_temp_table


def update_data(request):
    pass_to_temp_table()
    return HttpResponse("Parsing completed successfully")


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


@csrf_exempt
def get_next_heritage(request):
    if request.method == 'GET':
        heritage = ParsedData.objects.first()
        if heritage:
            data = {
                'name': heritage.name,
                'location': heritage.location,
                'year_whs': heritage.year_whs,
                'year_endangered': heritage.year_endangered
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'message': 'No pending objects'}, status=404)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def save_heritage(request):
    if request.method == 'POST':
        telebot_data = json.loads(request.body.decode('utf-8'))
        data = telebot_data.get('data')
        decision = telebot_data.get('decision')

        if data and decision:
            name = data.get('name')
            location = data.get('location')
            year_whs = data.get('year_whs')
            year_endangered = data.get('year_endangered')

            if name and location and year_whs and year_endangered:
                if decision == 'approve':
                    heritage = CulturalHeritage(name=name, location=location, year_whs=year_whs, year_endangered=year_endangered)
                    heritage.save()
                    ParsedData.objects.first().delete()
                    return JsonResponse({'message': 'Heritage saved successfully'})
                elif decision == 'reject':
                    ParsedData.objects.first().delete()
                    return JsonResponse({'message': 'Heritage rejected'})
                else:
                    return JsonResponse({'message': 'Invalid decision'}, status=400)
            else:
                return JsonResponse({'message': 'Missing required parameters'}, status=400)
        else:
            return JsonResponse({'message': 'Missing data or decision'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
