from django.shortcuts import render
from datetime import date, datetime
# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    text1 = request.POST.get('text1')
    length1 = len(text1)
    text2 = request.POST.get('text2')
    length2 = len(text2)
    text = request.POST.get('text')
    length = len(text)
    list_lenght = [length, length1, length2]
    max_list_lenght = max(list_lenght)
    return HttpResponse(max_list_lenght)


def index2(request):
    index_date = request.POST.get('date')
    date1 = datetime.strptime(index_date, '%Y-%m-%d')
    n_d = date1.strftime('%Y-01-01')
    if date1 == datetime.strptime(n_d, '%Y-%m-%d'):
        return HttpResponse(f'С новым {date1.year} годом!')
    else:
        return HttpResponse(f'{date1.year}-{date1.month}-{date1.day}')
