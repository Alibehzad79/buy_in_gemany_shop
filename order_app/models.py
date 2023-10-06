from django.db import models
from django.contrib.auth import get_user_model
from product_app.models import Product
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_("کاربر"), on_delete=models.CASCADE, related_name="orders")
    date_created = models.DateTimeField(_("تاریخ ایجاد"), auto_now=False, auto_now_add=False, blank=True, null=True)
    paid_price = models.CharField(_("هزینه پرداختی"), max_length=100, blank=True, null=True)
    is_paid = models.BooleanField(_("وضعیت پرداخت") ,default=False)
    full_price = models.CharField(_("قیمت کل"), max_length=100, editable=False)
    
    def full_price(self):
        amount = 0
        for item in self.items.all():
            amount += int(item.price) * item.count
    
        return amount
        
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = _("سبد خرید")
        verbose_name_plural = _("سبد خرید ها")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("سبد خرید"), on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE)
    price = models.CharField(_("قیمت"), max_length=100)
    count = models.IntegerField(_("تعداد"), default=1)
    date_add = models.DateTimeField(_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    
    
    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name = _("آیتم")
        verbose_name_plural = _("آیتم ها")