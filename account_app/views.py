from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from account_app.serializers import UserSerializer, UserDetail
from drf_spectacular.utils import extend_schema
# Create your views here.


@api_view(['POST'])
def register_user(request):      
    """
    {\n
        "username": "str",
        "email": "email@example.com",
        "password": "str",
        "phone_number": "09123456789"
    }
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_detail(request):
    user = request.user
    serializer = UserDetail(user)
    return Response(data=serializer.data)