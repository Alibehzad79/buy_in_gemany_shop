"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView
from config.views import home_page

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')), # for athentiace from api
    path('', home_page),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('products/', include('product_app.urls')),
    path('orders/', include('order_app.urls')),
    path('settings/', include('setting_app.urls')),
    path('accounts/', include('account_app.urls'),),
    path('dashboard/', include('account_app.dashboard_app.urls'), name='dashboard'),
    path('sliders/', include('slider_app.urls'),),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
]
