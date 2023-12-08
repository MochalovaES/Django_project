from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product, Category


def catalog_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        phone = request.POST.get('phone')
        print(f'{name} {text}: {phone}')
    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product


class CategoryListView(ListView):
    model = Category










