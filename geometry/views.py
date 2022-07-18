from django.shortcuts import redirect, render,HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def rectangle_area(request,width,height):
    area = width*height
    return render(request, 'geometry/rectangle.html', {'area': area, 'width': width, 'height': height})

def square_area(request,width):
    area = width**2
    return render(request, 'geometry/square.html', {'area': area, 'width': width})

def circle_area(request,radius):
    area = 3.14 * radius ** 2
    return render(request, 'geometry/circle.html', {'area': area, 'radius': radius})

def get_rectangle_area(request,width,height):
    redirect_url = reverse('rectangle_url', args=(width,height))
    return HttpResponseRedirect(redirect_url)

def get_square_area(request,width):
    redirect_url = reverse('square_url',args=(width,))
    return HttpResponseRedirect(redirect_url)

def get_circle_area(request,radius):
    redirect_url = reverse('circle_url', args=(radius,))
    return HttpResponseRedirect(redirect_url)
