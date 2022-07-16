from django.urls import path
from . import views

urlpatterns = [
    path('aries/', views.aries),
    path('taurus/', views.taurus),
]
