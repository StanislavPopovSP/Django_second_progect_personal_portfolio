from django.http import HttpResponse
from django.shortcuts import render
from .models import Skills # надо достать данные из БД, подключаем класс Skills

## Что бы обработчик сделал какую-то задачу, нам нужен URL.
def index(request) -> HttpResponse:
    """Обработчик главной страницы"""
    projects = Skills.objects.all() ## Хотим получить из объекта Skills все данные
    return render(request, 'skills/index.html', {'projects': projects})