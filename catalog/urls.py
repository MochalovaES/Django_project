from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_contacts, catalog_home, catalog_products

app_name = CatalogConfig.name

urlpatterns = [
    path('contact/', catalog_contacts, name='contacts'),
    path('home/', catalog_home, name='home'),
    path('', catalog_products, name='products'),
]
