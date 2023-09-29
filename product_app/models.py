from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.

class Product(models.Model):
    title = models.CharField(verbose_name=_('عنوان محصول'), max_length=100)
    content = HTMLField(verbose_name=_("توضیحات محصول"))
    image = models.ImageField(_("تصویر محصول"), upload_to="images/products/")
    price = models.BigIntegerField(_("قیمت محصول"))
    
    
    
    
    class Meta:
        verbose_name = _("محصول")
        verbose_name_plural = _("محصولات")