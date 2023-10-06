from django.urls import path
from order_app.views import order_list

urlpatterns = [
    path('order-list/', order_list, name='order-list'),
]
