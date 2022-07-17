from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_num>/', views.day_num),
    path('<str:day>/', views.day, name='day_url'),
    
]