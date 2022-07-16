from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse('Главная страница')

def posts(request):
    return HttpResponse('Все посты блога')
# Create your views here.
