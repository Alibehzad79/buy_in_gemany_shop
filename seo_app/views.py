from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from seo_app.models import ProductSeo
from seo_app.serializers import ProductSeoSerializer

# Create your views here.

@api_view(["GET"])
def product_seo_list(request):
    seos = ProductSeo.objects.all()
    serializer = ProductSeoSerializer(seos, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def product_seo_detail(request, *args, **kwargs):
    product_id = kwargs['product_id']
    try:
        seo =  ProductSeo.objects.get(id=product_id)
    except:
        return Http404()
    
    serializer = ProductSeoSerializer(seo)
    return Response(data=serializer.data, status=status.HTTP_200_OK)