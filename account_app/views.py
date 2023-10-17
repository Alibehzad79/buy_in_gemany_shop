from django.shortcuts import render, redirect
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
from account_app.forms import ResetPasswordFrom
from django.http import HttpResponse
from setting_app.models import Setting
from django.utils.translation import gettext_lazy as _
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
    setting = Setting.objects.last()
    url = setting.site_url
    user = get_user_model().objects.get(id=user_id)
    token = secrets.token_hex(256)
    user.reset_password_token = token
    user.save()
    status = send_mail(
            f"{setting.site_name} <no-replay>",
            f"برای بازیابی رمز عبور خود لینک زیر را باز کنید\n\nhttps://api.{url[8:]}accounts/reset-password-confirm/{token}/",
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

            send_email(email=email, user_id=user.id)
            return Response("ایمیل بازیابی ارسال شد", status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("متود باید POST باشد", status=status.HTTP_400_BAD_REQUEST)

def reset_password_confirm(request, *args, **kwargs):
    token = kwargs["token"]
    try:
        user = get_user_model().objects.get(reset_password_token=token)
    except:
        return HttpResponse('<h3 style="color: red;"> توکن نامعتبر </h3>')
    if request.method == "POST":
        form = ResetPasswordFrom(request.POST or None)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            print(user.username)
            user.set_password(password)
            user.reset_password_token = None
            user.save()
            return redirect('reset-password-done')
    else:
        form = ResetPasswordFrom()
    context = {
        'form': form,
    }
    return render(request, 'accounts/reset_password.html', context)

def passowrd_confirm_done(request):
    setting = Setting.objects.last()
    url = f"{setting.site_url}login/"
    context = {
        'url': url,
    }
    return render(request, 'accounts/reset_password_done.html', context)