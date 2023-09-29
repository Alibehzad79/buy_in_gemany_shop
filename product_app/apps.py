from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ProductAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_app'
    verbose_name = _("بخش پروژه")