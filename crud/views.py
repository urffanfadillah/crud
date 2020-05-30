from django.shortcuts import render
from django.views.generic import ListView

from core.models import Barang

class Home(ListView):
    template_name   = 'home.html'
    queryset        = Barang.objects.all() # <modelname>_list.html
