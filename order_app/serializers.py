from rest_framework import serializers
from order_app.models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    full_price = serializers.CharField()
    items = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = "__all__"
        
    
    def get_full_price(self, obj):
        return obj.full_price()
    
    def get_items(self, obj):
        return [OrderItemSerializer(s).data for s in obj.items.all()]