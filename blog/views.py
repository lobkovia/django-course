from django.shortcuts import render,HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from random import sample

allposts = [
    {
        'title': 'Рыбалка',
        'description': 'Хорошо посидели',
        'date': '21 авг 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Lorem ipsum dolor sit amet.'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
    },
]

def index(request):
    return render(request, 'blog/index.html', {'posts': sample(allposts, 3)})

def posts(request):
    return render(request, 'blog/list_detail.html',{})

def name_post(request,name_post):
    return render(request, 'blog/detail_by_name.html', {'name_post': name_post})

def number_post(request,number_post):
    return render(request, 'blog/detail_by_number.html', {'number_post': number_post})

def beautiful_table(request):
    return render(request, 'blog/beautiful_table.html')