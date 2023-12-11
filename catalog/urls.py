from django.urls import path

from catalog import views
from django.conf import settings
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from catalog.views import catalog_contacts, catalog_home, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contact/', catalog_contacts, name='contacts'),
    path('product/', ProductListView.as_view(), name='products_list'),
    path('', catalog_home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
