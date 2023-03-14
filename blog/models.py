from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) # Короткое поле, в котором можем указать максимальное кол-во символов 200
    description = models.TextField() # В данном поле будет описание. Для типа TextField не указывается максимальное кол-во символов.
    date = models.DateField() # Поле с датой, можно ни чего не указывать.

    ## Что бы экземпляр из views blog отображал корректно то что мы хотим в админке корректно,
    # нужно создать магический метод __str__. Нужно смотреть на тип данных, что бы был str.
    def __str__(self):
        """Возвращает поля в читаемом виде"""
        return self.title