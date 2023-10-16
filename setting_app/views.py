from django.shortcuts import render
from setting_app.serializers import SettingSerializer, ContactUsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from setting_app.models import Setting, ContactUs

# Create your views here.


@api_view(["GET"])
def settings(request):
    setting = Setting.objects.last()
    serializer = SettingSerializer(setting)
    return Response(serializer.data)


@api_view(["POST"])
def contact_us(request):
    """
        {
            \n
            "full_name": "str",
            "email": "email",
            "title": "str",
            "text": "str",
            "date_send": "str" -> like: "2023-10-13T22:08:28+03:30"
        }
    """
    contactus = ContactUs.objects.all()
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
