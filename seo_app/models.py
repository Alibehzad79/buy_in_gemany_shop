from django.db import models
from product_app.models import Product
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ProductSeo(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE, related_name="seos")
    description = models.CharField(_("توضیحات کوتاه"), max_length=160, help_text=_('حداکثر 160 کاراکتر'))
    keywords = models.TextField(_("کلمات کلیدی"))
    refresh = models.CharField(_("ریدایرکت"), max_length=200, help_text=_("e.g: 2;url=http://example.com"), blank=True, null=True, default=None)
    
    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name = _("سئو")
        verbose_name_plural = _("سئوی محصولات")
    