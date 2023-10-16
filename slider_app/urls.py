from django.urls import path
from slider_app.views import sliders

urlpatterns = [
    path('', sliders, name='sliders')
]
