from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_contacts, catalog_home, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contact/', catalog_contacts, name='contacts'),
    path('product/', ProductListView.as_view(), name='products_list'),
    path('', catalog_home, name='home'),
]
