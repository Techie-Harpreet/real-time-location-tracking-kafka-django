from django.shortcuts import render
from home.models import *
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def get_data(request):
    latest_data = LocationUpdate.objects.latest('timestamp')
    data = {
        'latitude': latest_data.latitude,
        'longitude': latest_data.longitude,
        'timestamp': latest_data.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    }
    return JsonResponse(data)
