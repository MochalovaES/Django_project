from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.forms import ProductForm, VersionForm, ModeratorForm
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

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        for object in context['product_list']:
            active_version = Version.objects.filter(product=object, is_active=True).last()
            if active_version:
                object.active_version_number = active_version.number_version
                object.name_version = active_version.name_version
            else:
                object.active_version_number = None
        return context


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_validate(self, form):
        response = super().form_valid(form)
        self.object.owner = self.request.user
        self.object.save()
        return response


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:index')

    def get_form_class(self):
        if self.request.user.is_staff:
            return ModeratorForm
        else:
            return ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = version_formset(self.request.POST, instance=self.object)
        else:
            formset = version_formset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_list')

