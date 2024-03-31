from django.urls import path

from .views import (Supplylist,
                     CategoryList, 
                    SupplyDetail, 
                    SupplyCreateView, 
                    CategoryCreateView, 
                    SizeCreateView, 
                    ColorCreateView, 
                    search_view
                    )


app_name = 'goods'
urlpatterns = [
    path('', Supplylist.as_view(), name='supply_list'), 
    path('category/', CategoryList.as_view(), name='category_list'),
    path('detail/<id>', SupplyDetail.as_view(), name='supply_detail'), 
    path('create_supply/', SupplyCreateView.as_view(), name='supply_create'), 
    path('create_category/', CategoryCreateView.as_view(), name='category_create' ), 
    path('create_color/', ColorCreateView.as_view(), name='color_create' ),
    path('create_size/', SizeCreateView.as_view(), name='size_create' ), 
    path ('search/', search_view, name='search'), 
]

