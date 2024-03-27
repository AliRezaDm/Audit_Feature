from django.urls import path
from .views import Supplylist, CategoryList, SupplyDetail, SupplyCreateView, CategoryCreateView


app_name = 'goods'
urlpatterns = [
    path('', Supplylist.as_view(), name='supply_list'), 
    path('category/', CategoryList.as_view(), name='category_list'),
    path('detail/<id>', SupplyDetail.as_view(), name='supply_detail'), 
    path('create_supply/', SupplyCreateView.as_view(), name='supply_create'), 
    path('create_category/', CategoryCreateView.as_view(), name='category_create' )
]

