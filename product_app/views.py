from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.http import Http404
from product_app.models import Product
from product_app.serializers import ProductSerializer, CommentSerializer
import datetime
import json
# Create your views here.

class ProductListAPIview(APIView):
    """
        List of product
    """
    
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    
    """
        Detail of product
    """
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            raise Http404()
    
    def get(self, request, pk, slug, format=None):
        product = self.get_object(pk)
        product.visit_count += 1
        product.save()
        serializer = ProductSerializer(product)
        related_product = Product.objects.filter(category__slug=product.category.slug, status='avalible').distinct().all()[:4]
        related_products = []
        for product in related_product:
            related_products.append({'id': product.id, 'title': product.title,  'slug': product.slug, 'image': product.image.url, 'price': product.price})
        context = [
            {'product': serializer.data},
            {'related_products': related_products}
        ]
        
        return Response(context)

class CommentAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)    