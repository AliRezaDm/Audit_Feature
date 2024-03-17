from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Supply

class Supplylist(ListView):

    model = Supply
    queryset = Supply.objects.Available()
    template_name = 'goods/supply_list.html'