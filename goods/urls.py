from django.urls import path
from .views import Supplylist, CategoryList


app_name = 'goods'
urlpatterns = [
    path('', Supplylist.as_view(), name='supply_list'), 
     path('category/', CategoryList.as_view(), name='category_list')
]

