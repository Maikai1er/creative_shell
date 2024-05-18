import json

from django.http import JsonResponse, HttpResponse, HttpRequest
from django.db.models.functions import Random
from django.views.decorators.csrf import csrf_exempt

from cultural_heritage.models import CulturalHeritage
from parser.models import ParsedData
from parser.parser import parse_and_save_to_temp_table

from . import data_management


def update_data(request: HttpRequest) -> HttpResponse:
    parse_and_save_to_temp_table()
    return HttpResponse("Parsing completed successfully")


def load_more_heritages(request: HttpRequest) -> JsonResponse:

    heritages = CulturalHeritage.objects.all().order_by(Random())[:5]

    data = [{
        'name': heritage.name,
        'location': heritage.location,
        'year_whs': heritage.year_whs,
        'year_endangered': heritage.year_endangered
    } for heritage in heritages]

    return JsonResponse(data, safe=False)


def index(request: HttpRequest) -> JsonResponse:
    heritages = CulturalHeritage.objects.all().order_by(Random())[:5]

    data = [{
        'name': heritage.name,
        'location': heritage.location,
        'year_whs': heritage.year_whs,
        'year_endangered': heritage.year_endangered
    } for heritage in heritages]

    return JsonResponse(data, safe=False)


@csrf_exempt
def get_next_heritage(request: HttpRequest) -> JsonResponse:
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
def save_heritage(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        try:
            telebot_data = json.loads(request.body.decode('utf-8'))
            heritage = telebot_data.get('data')
            decision = telebot_data.get('decision')

            if not (heritage and decision):
                raise ValueError('Missing data or decision')

            name = heritage.get('name')
            location = heritage.get('location')
            year_whs = heritage.get('year_whs')
            year_endangered = heritage.get('year_endangered')

            if not (name and location and year_whs and year_endangered):
                raise ValueError('Missing required parameters')

            if decision == 'approve':
                data_management.save_to_heritage_table(heritage)
                ParsedData.objects.first().delete()
                return JsonResponse({'message': 'Heritage saved successfully'})
            elif decision == 'reject':
                ParsedData.objects.first().delete()
                return JsonResponse({'message': 'Heritage rejected'})
            else:
                return JsonResponse({'message': 'Invalid decision'}, status=400)
        except ValueError as ve:
            return JsonResponse({'message': str(ve)}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred: {}'.format(str(e))}, status=500)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def receive_contact_data(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        try:
            contact_data = json.loads(request.body.decode('utf-8'))
            name = contact_data.get('name')
            contact = contact_data.get('contact')
            about = contact_data.get('about')

            if not (name and contact and about):
                raise ValueError('Missing required data')

            data_management.save_to_contact_data_table(contact_data)
            return JsonResponse({'message': 'Contact data saved successfully'})

        except ValueError as ve:
            return JsonResponse({'message': str(ve)}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred: {}'.format(str(e))}, status=500)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
