from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView 
from .models import Supply, Category





class Supplylist(ListView):

    model = Supply
    queryset = Supply.objects.Available()
    template_name = 'goods/supply_list.html'

class SupplyDetail(DetailView):

    model = Supply
    template_name = 'goods/supply_detail.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Supply.objects.Available(), pk=id)
   
class CategoryList(ListView):

    model = Category
    queryset = Category.objects.filter(status=True)
    template_name = "goods/category_list"