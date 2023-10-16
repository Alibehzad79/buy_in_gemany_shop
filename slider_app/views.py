from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from slider_app.models import Slider
from slider_app.serializers import SliderSerializer
# Create your views here.

@api_view(["GET"])
def sliders(request):
    slider = Slider.objects.filter(active=True).all()
    serializer = SliderSerializer(slider, many=True)
    return Response(serializer.data)