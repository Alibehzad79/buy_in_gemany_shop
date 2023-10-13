from django.urls import path
from order_app.views import OrderAPIView, PaidOrderAPIView, BankPaySerializerAPIView

urlpatterns = [
    path('', OrderAPIView.as_view(), name='order'),
    path('orders-paid/', PaidOrderAPIView.as_view(), name="paid-orders"),
    path('bank-pay/', BankPaySerializerAPIView.as_view(), name="bank-pay"),
]