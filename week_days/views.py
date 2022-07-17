from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

days = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday' : 4,
        'friday' : 5,
        'saturday' :6 ,
        'sunday' : 7
    }
def day(request, day):

    if day in days:
        return HttpResponse(f'Задачи на {day}')
    else:
        return HttpResponse(f'День недели {day} не существует')


def day_num(request,day_num):
    if day_num in list(days.values()):
        day = list(days.items())[day_num - 1][0]
        redirect_url = reverse('day_url',args=(day))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponse(f'Неверный номер дня - {day_num}')