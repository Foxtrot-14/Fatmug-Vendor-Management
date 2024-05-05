from .models import Vendor,PurchaseOrder
from rest_framework import serializers
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
     
    class PurchaseOrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = PurchaseOrder
            fields = '__all__'
            read_only_fields = [' order_date', 'delivery_date', 'actual_delivery_date', 'status','quality_rating','issue_date','acknowledgment_date','delayed']