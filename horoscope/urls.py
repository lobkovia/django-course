from django.urls import path
from . import views

urlpatterns = [
    path('aries/', views.aries),
    path('taurus/', views.taurus),
    path('type/', views.hor_type),
    path('type/<element>', views.hor_element, name='hor_element_url'),
]
