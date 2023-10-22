from django.urls import path
from seo_app.views import product_seo_list, product_seo_detail

urlpatterns = [
    path('', product_seo_list, name="seos"),
    path('<int:product_id>/', product_seo_detail, name="seos"),
]
