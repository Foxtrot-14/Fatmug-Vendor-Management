from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('vendors/', vendor_list,name='vendors_list'),
]