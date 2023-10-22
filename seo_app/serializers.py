from rest_framework import serializers
from seo_app.models import ProductSeo

class ProductSeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSeo
        fields = "__all__"