import csv

from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    # получите текущую страницу и передайте ее в контекст


    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', encoding='UTF8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        stations_list = list(reader)
        paginator = Paginator(stations_list, 20)
        page = paginator.get_page(page_number)



    context = {
         'bus_stations': page.object_list,
         'page': page,

    }
    return render(request, 'stations/index.html', context)
