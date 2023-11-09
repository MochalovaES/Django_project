from django.urls import path

from catalog.views import catalog_contacts, catalog_home

urlpatterns = [
    path('', catalog_contacts),
    path('', catalog_home),
]