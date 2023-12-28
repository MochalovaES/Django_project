from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact/', catalog_contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product_form/', ProductCreateView.as_view(), name='add_product'),
    path('product_form/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
]
