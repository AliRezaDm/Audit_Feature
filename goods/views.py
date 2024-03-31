from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Supply, Category, Size, Color
from .forms import SearchForm




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
   
class SupplyCreateView(CreateView):

    model = Supply
    fields = ['title', 'category', 'count', 'image', 'color', 'size']
    template_name = 'goods/add_supply_form.html'


class CategoryList(ListView):

    model = Category
    queryset = Category.objects.filter(status=True)
    template_name = "goods/category_list"

class CategoryCreateView(CreateView):

    model = Category
    fields = ['parent', 'title', 'status']
    template_name = "goods/add_category_form.html"

class SizeCreateView(CreateView):

    model = Size
    fields = ['name']
    template_name = "goods/add_size_form.html"

class ColorCreateView(CreateView):

    model = Color
    fields = ['name']
    template_name = "goods/add_color_form.html"


@require_POST
def search_view(request):
    
    supply_query =Supply.objects.Available()
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            data = search_form.cleaned_data['search']
            supply = supply_query.filter(Q(title__icontains = data) | Q(description__icontains = data))
            
            return render(request, 'goods/supply_list.html', {"Supply": supply, "search_form": search_form})