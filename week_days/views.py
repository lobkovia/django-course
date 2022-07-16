from django.shortcuts import render,HttpResponse


def monday(request):
    return HttpResponse('Задачи на понедельник')

def tuesday(request):
    return HttpResponse(' Задачи на вторник')
# Create your views here.
