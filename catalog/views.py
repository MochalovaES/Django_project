from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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
    form_class = ProductForm
    template_name = 'catalog/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)