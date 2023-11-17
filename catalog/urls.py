from django.urls import path

from catalog.views import catalog_contacts, catalog_home

urlpatterns = [
    path('contact/', catalog_contacts, name='contacts'),
    path('home/', catalog_home, name='home'),
]
