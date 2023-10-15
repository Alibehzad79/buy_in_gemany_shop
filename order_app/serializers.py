from rest_framework import serializers
from order_app.models import Order, PaidOrder, BankPay
from django.http import HttpResponse

class OrderSerializer(serializers.ModelSerializer):
    full_price = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = ("id", "date_created", "count", "user", "product", "full_price")
        
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

class PaidOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidOrder
        exclude = ('complete',)
    
    def create(self, validate_data):
        pain_order = PaidOrder(
            count=validate_data["count"],
            payment=validate_data["payment"],
            full_name=validate_data["full_name"],
            phone_number=validate_data["phone_number"],
            post_code=validate_data["post_code"],
            address=validate_data["address"],
            tracking_code=validate_data["tracking_code"],
            date_created=validate_data["date_created"],
            status=validate_data["status"],
            user=validate_data["user"],
            order=validate_data["order"],
            product=validate_data["product"]
        )
        pain_order.save()
        return pain_order

class BankPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = BankPay
        fields = "__all__"
    
    def create(self, validate_data):
        bank_pay = BankPay(
            user=validate_data["user"],
            order=validate_data["order"],
            code=validate_data["code"],
            ref_id=validate_data["ref_id"],
            card_pan=validate_data["card_pan"],
            card_hash=validate_data["card_hash"],
            fee_type=validate_data["fee_type"],
            fee=validate_data["fee"],
            date_created=validate_data["date_created"]
        )
        bank_pay.save()
        return bank_pay
    
# TODO PaidOrder, BankPay