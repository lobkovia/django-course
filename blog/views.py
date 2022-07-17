from django.shortcuts import render,HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect


def index(request):
    return HttpResponse('Главная страница')

def posts(request):
    return HttpResponse('Все посты блога')
# Create your views here.
def name_post(request,name_post):
    return HttpResponse(f'Информация о посте {name_post}')

def number_post(request,number_post):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')