from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog

# def blogs(request) -> HttpResponse:
#     blog = Blog.objects.all() # Получаем доступ к модели, мы из модели Blog берем все записи которые есть в таблице Blog. К ним мы можем обратиться по ключу словаря в html шаблоне.
#     return render(request, 'blog/blogs.html', {'blogs': blog}) # В шаблоне будем использовать ключ

## Если нам надо отсортировать по дате, то нам нужен метод order_by и он будет принимать поле data. Данный метод отработает так же как и all, но + будет сортировка.
## Для того что бы сделать по убыванию нужно прописать - перед полем.
def blogs(request) -> HttpResponse:
    blog = Blog.objects.order_by('-date') # Самая первая дата будет, самая ранняя кот-я есть.
    return render(request, 'blog/blogs.html', {'blogs': blog})

## Пишем представление detail, функция будет принимать еще blog_id
# get_object_or_404 - получить объект или ошибку 404 если у нас такого элемента нету. Это что бы выводились только те данные которые у нас есть. Первым параметром она принимает имя нашего модуля, вторым параметром pk= это primary key
def detail(request, blog_id):
    """Будет возвращать отдельную страничку"""
    blog = get_object_or_404(Blog, pk=blog_id) # Если в БД в модуле Blog есть наш id, то он попадет в pk, тогда в blog вернется сам объект, то мы его можем вывести по необходимости. А если не будет такого номера, тогда будет возвращаться ошибка 404, что такой страницы не существует.
    return render(request, 'blog/details.html', {'blog': blog}) # третим параметром передадим то как мы его можем вывести на html страничке.
