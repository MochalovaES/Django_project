from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Зелень', 'description': 'Свежая зелень'},
            {'name': 'Орех', 'description': 'Высушенные орехи'},
            {'name': 'Орех обжаренный', 'description': 'Обжаренные орехи'},
        ]
        Category.objects.all().delete()

        for category in category_list:
            Category.objects.create(**category)

