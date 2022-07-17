from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/<int:number_post>/', views.number_post),
    path('posts/', views.posts),
    path('posts/<name_post>/', views.name_post),
    
]