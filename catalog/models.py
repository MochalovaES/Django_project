from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='изображение')
    category = models.CharField(max_length=150, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateField(**NULLABLE, verbose_name='дата создания')
    last_date = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}: {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


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

