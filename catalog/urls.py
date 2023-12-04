from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_contacts, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contact/', catalog_contacts, name='contacts'),
    path('home/', CategoryListView.as_view(), name='home'),
    path('', CategoryListView.as_view(), name='products'),
]
