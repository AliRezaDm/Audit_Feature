from django.urls import path

from .views import (Supplylist,
                     CategoryList, 
                    SupplyDetail, 
                    SupplyCreateView, 
                    SupplyUpdateView, 
                    SupplyDeleteView, 
                    CategoryCreateView, 
                    SizeCreateView, 
                    ColorCreateView, 
                    search_view
                    )


app_name = 'goods'
urlpatterns = [
    # Supply Urls
    path('', Supplylist.as_view(), name='supply_list'), 
    path('detail/<id>', SupplyDetail.as_view(), name='supply_detail'), 
    path('create_supply/', SupplyCreateView.as_view(), name='supply_create'), 
    path('update_supply/<id>', SupplyUpdateView.as_view(), name='supply_update'), 
    path('delete_supply/<id>', SupplyDeleteView.as_view(), name='supply_delete'),
    
    # Category Urls  
    path('category/', CategoryList.as_view(), name='category_list'),
    path('create_category/', CategoryCreateView.as_view(), name='category_create' ), 

    # Color Urls
    path('create_color/', ColorCreateView.as_view(), name='color_create' ),

    # Size Urls
    path('create_size/', SizeCreateView.as_view(), name='size_create' ), 

    # Search Url
    path ('search/', search_view, name='search'), 
    
]

    