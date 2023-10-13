from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from order_app.serializers import OrderSerializer, PaidOrderSerializer, BankPaySerializer
from order_app.models import Order
from datetime import datetime

# Create your views here.

class OrderAPIView(APIView):
    """
    [
        \n
        {
            "date_created": str -> like: "2023-10-13T21:30:21+03:30",
            "count": int,
            "user": int,
            "product": int
        },
        {
            "date_created": str -> like: "2023-10-13T21:30:21+03:30",
            "count": int,
            "user": int,
            "product": int
        }
    ]
    
    """
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user_id = request.user.id
        user = get_user_model().objects.get(id=user_id)
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


class PaidOrderAPIView(APIView):
    """ 
    {
        \n
        "id": int,
        "count": int,
        "payment": str,
        "full_name": str,
        "phone_number": str,
        "post_code": str,
        "address": str,
        "tracking_code": str,
        "date_created": str -> like: "2023-10-13T22:08:28+03:30",
        "status": bool,
        "order": int,
        "user": int,
        "product": int
    }
    
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user_id = request.user.id
        user = get_user_model().objects.get(id=user_id)
        orders = user.orders_pay.all()
        serializer = PaidOrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PaidOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

class BankPaySerializerAPIView(APIView):
    """
    {
        \n
        "code": int,
        "ref_id": int,
        "card_pan": str,
        "card_hash": str,
        "fee_type": str,
        "fee": int,
        "date_created": str -> like: "2023-10-13T22:19:38+03:30",
        "user": int,
        "order": int
    }
    
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = BankPaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)