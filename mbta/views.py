from django.shortcuts import render
from django.http import HttpResponse
import requests


# url: 'https://api-v3.mbta.com/routes'
def subways(request):
    url = 'https://api-v3.mbta.com/routes'
    response = requests.get(url)
    data = response.json()
    subways = {}
    for d in data['data']:
        subways[d['id']] = d['attributes']['long_name']
    return render(request, 'subways.html', {'subways': subways})


def subway_stops(request, subway_id):
    url = f'https://api-v3.mbta.com/stops?filter[route]={subway_id}'
    response = requests.get(url)
    data = response.json()
    stops = []
    for d in data['data']:
        stops.append(d['attributes']['address'])
    return render(request, 'subway_stops.html', {'stops': stops})
