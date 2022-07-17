from django.urls import path
from . import views


urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.rectangle_area, name='rectangle_url'),
    path('square/<int:width>/', views.square_area, name='square_url'),
    path('circle/<int:radius>/', views.circle_area, name='circle_url'),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area),
    path('get_square_area/<int:width>/', views.get_square_area),
    path('get_circle_area/<int:radius>/', views.get_circle_area),
]