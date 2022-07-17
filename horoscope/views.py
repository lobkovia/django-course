from django.shortcuts import render,HttpResponse
from django.http import HttpRequest, HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse

elements = {
    'fire':['Aries','Leo','Saggitarius'],
    'water': ['Pisces','Scorpio','Cancer'],
    'air': ['Libra','Aquarius','Gemini'],
    'earth': ['Taurus','Virgo','Capricorn']
}

def aries(request):
    return HttpResponse('Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).')

def taurus(request):
    return HttpResponse(' Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).')

def hor_type(request):
    resp=''
    for el in elements:
        redirect_url = reverse('hor_element_url',args=(el,))
        resp += f'<h1><li><a href="{redirect_url}">{el.title()}<a></li></h1>'
    return HttpResponse(resp)

def hor_element(request, element):
    if element in elements:
        resp=''
        for el in elements[element]:
            resp += f'<h1><li>{el}</li></h1>'
        return HttpResponse(resp)
    else:
        return HttpResponseNotFound(f'Нет такого элемента - {element}')