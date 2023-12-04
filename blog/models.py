from django.db import models


NULLABLE = {'null': True, 'blank': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    image_blog = models.ImageField(upload_to='article/', **NULLABLE, verbose_name='изображение')
    date_created = models.DateField(**NULLABLE, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    number_views = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'
