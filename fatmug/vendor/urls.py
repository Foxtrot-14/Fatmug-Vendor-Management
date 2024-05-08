from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('vendors/', vendor_list,name='vendors_list'),
    path('vendors/<int:vendor_id>', get_vendor,name='get_vendor'),
    path('vendors/<int:vendor_id>/performance', get_performance,name='get_vendor'),
    path('purchase_orders/', po_list,name='po_list'),
    path('purchase_orders/<int:po_id>', get_po,name='get_po'),
]