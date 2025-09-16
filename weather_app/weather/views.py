from .services import get_weather_data
from django.http import JsonResponse
from django.shortcuts import render

def fetch_weather(request):
    # print(get_weather_data('ho chi minh'))
    if not request.GET:
        return render(request, 'index.html')
    location, day_index = request.GET.get('location'), request.GET.get('day')
    data = get_weather_data(location, day_index)
    if not data:
        return JsonResponse(_response(False, None, 'Data not found'), status=404)
    else:
        return JsonResponse(_response(True, data))

def _response(success: bool, data: dict|None = None, error: str|None = None):
    return {'success': success, 'data': data, 'error': error}