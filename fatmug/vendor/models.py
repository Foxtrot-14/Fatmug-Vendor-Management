from datetime import timezone
from django.db import models
from django.utils import timezone
# Create your models here.
class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact_details = models.TextField(max_length=150)
    address = models.TextField(max_length=100)
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(null=True)  
    quality_rating_avg = models.FloatField(null=True)  
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)
    
    def save(self, *args, **kwargs):
        super(Vendor, self).save(*args, **kwargs)
        hp_entries = HistoricalPerformance.objects.filter(vendor=self)
        for hp_entry in hp_entries:
            hp_entry.on_time_delivery_rate = self.on_time_delivery_rate
            hp_entry.quality_rating_avg = self.quality_rating_avg
            hp_entry.average_response_time = self.average_response_time
            hp_entry.fulfillment_rate = self.fulfillment_rate
            hp_entry.save()
    
    def update_on_time_delivery_rate(self):
        completed_orders_count = self.purchase_order.filter(status='completed').count()
        on_time_orders_count = self.purchase_order.filter(status='completed', delayed=False).count()
        self.on_time_delivery_rate = (on_time_orders_count / completed_orders_count) * 100 if completed_orders_count > 0 else 0
        self.save()
    
    def update_quality_rating_avg(self):
        completed_orders = self.purchase_order.filter(status='completed', quality_rating__isnull=False)
        quality_rating_sum = sum(order.quality_rating for order in completed_orders)
        completed_orders_count = completed_orders.count()
        self.quality_rating_avg = quality_rating_sum / completed_orders_count if completed_orders_count > 0 else 0
        self.save()
    
    def update_average_acknowledgment_time(self):
        total_time_difference = timezone.timedelta(0)
        acknowledged_orders = self.purchase_order.filter(acknowledgment_date__isnull=False)
        for order in acknowledged_orders:
            time_difference = order.acknowledgment_date - order.issue_date
            total_time_difference += time_difference
        total_orders_count = acknowledged_orders.count()
        self.average_acknowledgment_time = total_time_difference / total_orders_count if total_orders_count > 0 else timezone.timedelta(0)
        self.save()    
    
    def update_fulfilment_rate(self):
        total_orders_count = self.purchase_order.count()
        fulfilled_orders_count = self.purchase_order.filter(status='completed', delayed=False).count()
        self.fulfilment_rate = (fulfilled_orders_count / total_orders_count) * 100 if total_orders_count > 0 else 0
        self.save()
             
    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    id = models.AutoField(primary_key=True)
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_order')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(verbose_name="Expected delivery date")
    actual_delivery_date = models.DateTimeField(null=True, blank=True, verbose_name="Actual delivery date")
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    delayed = models.BooleanField(default=False, verbose_name="Delayed")
    
    def __str__(self):
        return self.po_number
         
    def save(self, *args, **kwargs):
        self.vendor.update_fulfilment_rate()
        if self.status == 'completed':
            self.actual_delivery_date = timezone.now() 
            if self.actual_delivery_date > self.expected_delivery_date:
                self.delayed = True
        super().save(*args, **kwargs)
        if self.status == 'completed':
            self.vendor.update_on_time_delivery_rate()
            self.vendor.update_quality_rating_avg()
        if self.acknowledgment_date is not None:
            self.vendor.update_average_acknowledgment_time()        

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performances')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    def __str__(self):
        return f"{self.vendor.name} - {self.date}"        
