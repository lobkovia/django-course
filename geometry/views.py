from django.shortcuts import redirect, render,HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def rectangle_area(request,width,height):
    area = width*height
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {area}')

def square_area(request,width):
    area = width**2
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {area}')

def circle_area(request,radius):
    area = 3.14 * radius ** 2
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {area}')

def get_rectangle_area(request,width,height):
    redirect_url = reverse('rectangle_url', args=(width,height))
    return HttpResponseRedirect(redirect_url)

def get_square_area(request,width):
    redirect_url = reverse('square_url',args=(width,))
    return HttpResponseRedirect(redirect_url)

def get_circle_area(request,radius):
    redirect_url = reverse('circle_url', args=(radius,))
    return HttpResponseRedirect(redirect_url)
