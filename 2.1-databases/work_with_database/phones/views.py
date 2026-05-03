import csv
from .models import Phone

from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return redirect('catalog')

def show_catalog(request):

    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    sort_order = 'name'  # Значение по умолчанию

    if sort == 'min_price':
       sort_order = 'price'
    elif sort == 'max_price':
        sort_order = '-price'

    phones = Phone.objects.all().order_by(sort_order)

    context = {
        'phones': phones,
        'sort' : sort,
    }
    return render(request,template, context)
#
#
def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)


    context = {
        'phone': phone,
    }
    return render(request, template, context)
