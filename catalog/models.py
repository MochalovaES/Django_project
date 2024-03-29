from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')
    is_active = models.BooleanField(default=True, verbose_name='есть в наличии')
    #created_at = models.CharField(max_length=150, **NULLABLE, verbose_name='место изготовления')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория ID', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за шт.')
    creation_date = models.DateField(verbose_name='Дата создания', default='2023-01-01')
    last_date = models.DateField(verbose_name='Дата последнего изменения', default='2023-01-01')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name } {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_version = models.IntegerField(verbose_name="Номер версии")
    name_version = models.CharField(max_length=150, verbose_name="Название версии")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product} {self.name_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        unique_together = (('number_version', 'product'),)
