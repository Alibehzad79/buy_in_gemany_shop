from django.urls import path
from product_app.views import ProductListAPIview, ProductDetailAPIView, CommentAPIView

urlpatterns = [
    path('', ProductListAPIview.as_view(), name="products_list"),
    path('<int:pk>/<slug:slug>/', ProductDetailAPIView.as_view(), name="products_detail"),
    path('comment/', CommentAPIView.as_view(), name='comment')
]
