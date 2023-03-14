"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # импортируем static сюда в наш документ, это как метод
from django.conf import settings # он будет автоматически поймет что это настройки и будет и будет их брать из документа settings.
from skills import views

## Это как основной домен
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # '' - путь к главной странице.
    path('blog/', include('blog.urls')), # после странички блог надо обязательно поставить слеш,
    # после каждого указания пути нужно ставть слешь, без слеша будет работать когда
    # это конечная страница. Если с этой страницы нужно перейти дальше на вложенные элементы дожен быть слеш.
    # Если мы делаем ссылку на другое приложение, там своих путей может быть очень много. Поэтому
    # отдельное приложение описывается в отдельном URL, но что бы его можно было отдельно подключить
    # там где from django.urls import path должны добавить модуль include.
    # В include мы будем подключать в кавычках приложение 'blog' и из него будем брать urls. Это обычный путь.
]

# Эта часть всегда пишется в корневом urls. Корневой URL всегда совпадает по названию имя проекта с папкой где будут глобальные настройки. И в ней глобальный URL самый главный.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # document_root - именованный параметр. Если в нашем приложении есть какие-та изображения они выводятся, и попадают в БД должны быть обязательно такая строка.
