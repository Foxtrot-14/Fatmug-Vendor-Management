from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from .serializer import VendorSerializer,PurchaseOrderSerializer,HistoricalPerformanceSerializer

@api_view(['GET','POST'])
def vendor_list(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def get_vendor(request, vendor_id):
    if request.method == 'GET':
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            serializer = VendorSerializer(vendor, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            vendor.delete()
            return Response({"msg":"Vendor Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET','POST'])
def po_list(request):
    if request.method == 'GET':
        vendors = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(vendors, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET','PUT','DELETE'])
def  get_po(request,po_id):
    if request.method == 'GET':
        try:
            po = PurchaseOrder.objects.get(id=po_id)
            serializer = PurchaseOrderSerializer(po)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)  
    elif request.method == 'PUT':
        try:
            po = PurchaseOrder.objects.get(id=po_id)
            serializer = PurchaseOrderSerializer(po, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            po = PurchaseOrder.objects.get(id=po_id)
            po.delete()
            return Response({"msg":"Purchase Order Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_performance(request,vendor_id):
    if request.method == 'GET':
        try:
            hp = HistoricalPerformance.objects.get(vendor=vendor_id)
            serializer = HistoricalPerformanceSerializer(hp)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except HistoricalPerformance.DoesNotExist:
            return Response({"error": "Historical Performance not found"}, status=status.HTTP_404_NOT_FOUND)
