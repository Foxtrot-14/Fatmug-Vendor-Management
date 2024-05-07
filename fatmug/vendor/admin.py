from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'vendor_code']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['id','po_number', 'vendor', 'delivery_date', 'status']
    list_filter = ['vendor', 'status']
    search_fields = ['po_number', 'vendor__name']

@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
    list_filter = ['vendor']
    search_fields = ['vendor__name']
