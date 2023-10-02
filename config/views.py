from django.shortcuts import redirect, HttpResponse
from config import settings
from django.http import Http404

def home_page(request):
    if not settings.DEBUG:
        return redirect('swagger-ui')