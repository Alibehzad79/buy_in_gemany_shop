from django.urls import path
from setting_app.views import settings, contact_us

urlpatterns = [
    path('', settings, name="settings"),    
    path('contact-us/', contact_us, name="contact-us"),    
]
