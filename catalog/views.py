from django.shortcuts import render

from catalog.models import Product


def catalog_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        phone = request.POST.get('phone')
        print(f'{name} {text}: {phone}')
    return render(request, 'catalog/contacts.html')


def catalog_home(request):
    context = {
        'object_list_': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', context)


def catalog_products(request):
    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/products.html', context)








