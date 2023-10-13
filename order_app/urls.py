from django.urls import path
from order_app.views import OrderAPIView

urlpatterns = [
    path('', OrderAPIView.as_view(), name='order'),
]