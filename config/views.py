from django.shortcuts import redirect
from setting_app.models import Setting

def home_page(request):
    setting = Setting.objects.last()
    url = setting.site_url
    return redirect(url)