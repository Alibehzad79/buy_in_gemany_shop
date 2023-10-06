from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from order_app.serializers import OrderSerializer
from order_app.models import Order
# Create your views here.


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def order_list(request):
    user_id = request.user.id
    user = get_user_model().objects.get(id=user_id)
    orders = user.orders.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def add_item(request):
#     user_id = request.user.id
#     user = get_user_model().objects.get(id=user_id)
#     order = user.orders.filter(is_paid=False).last()
    