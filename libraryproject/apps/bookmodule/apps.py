from django.apps import AppConfig
from django.shortcuts import render

class UsermoduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bookmodule'

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')
