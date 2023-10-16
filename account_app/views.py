from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from account_app.serializers import UserSerializer, UserDetail, RestPasswordSerializer
from drf_spectacular.utils import extend_schema
from django.core.mail import send_mail
from config import settings
import secrets
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


def send_email(user_id, email):
    user = get_user_model().objects.get(id=user_id)
    token = secrets.token_hex(256)
    user.reset_password_token = token
    user.save()
    status = send_mail(
            "بازیابی رمز عبور",
            f"http://127.0.0.1:8000/accounts/rest-password/{token}/",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

@api_view(["POST"])
def get_reset_password(request, *args, **kwargs):
    if request.method == "POST":
        serializer = RestPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            try:
                user = get_user_model().objects.get(email=email)
            except:
                return Response('کاربری یافت نشد', status=status.HTTP_400_BAD_REQUEST)
            if get_user_model().objects.filter(email=email).exists():
                send_email(email=email, user_id=user.id)
                return Response("ایمیل بازیابی ارسال شد", status=status.HTTP_200_OK)
            else:
                return Response('ایمیل نامعتبر است.', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

