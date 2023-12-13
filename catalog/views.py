from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


def catalog_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        phone = request.POST.get('phone')
        print(f'{name} {text}: {phone}')
    return render(request, 'catalog/contacts.html')


def catalog_home(request):
    context_ = {
        'object_list_': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', context_)



#def catalog_products(request):
#    context = {
#        'object_list': Product.objects.all(),
#    }
#    return render(request, 'catalog/products_list.html', context)




class ProductListView(ListView):
    paginate_by = 6
    model = Product
    template_name = 'catalog/product_list.html'
    extra_context = {
        'objects_list': Product.objects.all()
    }


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
