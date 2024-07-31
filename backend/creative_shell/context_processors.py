from django.conf import settings
from django.http import HttpRequest


def api_host(request: HttpRequest) -> dict:
    return {'API_HOST': settings.API_HOST}
