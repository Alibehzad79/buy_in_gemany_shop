from rest_framework import serializers
from order_app.models import Order, PaidOrder, BankPay

class OrderSerializer(serializers.ModelSerializer):
    full_price = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = ("date_created", "count", "user", "product", "full_price")
        
    def get_full_price(self, obj):
        return obj.full_price()

    def create(self, validate_data):
        
        order = Order(
            user=validate_data['user'],
            count=validate_data['count'],
            date_created=validate_data['date_created'],
            product=validate_data['product']
        )
        order.save()
        return order


# TODO PaidOrder, BankPay