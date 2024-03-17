from django.urls import path
from .views import Supplylist



urlpatterns = [
    path('', Supplylist.as_view(), name='supply_list')
]

