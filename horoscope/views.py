from django.shortcuts import render,HttpResponse
from django.http import HttpRequest, HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse

elements = {
    'fire':['Aries','Leo','Saggitarius'],
    'water': ['Pisces','Scorpio','Cancer'],
    'air': ['Libra','Aquarius','Gemini'],
    'earth': ['Taurus','Virgo','Capricorn']
}

peoples = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
]

peoples_detail = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]

def people(request):
    return render(request, 'horoscope/people.html', {'peoples': peoples})
    
def people_detail(request):
    return render(request, 'horoscope/people_detail.html', {'peoples': peoples_detail})

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