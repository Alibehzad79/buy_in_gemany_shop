from django.db import models
from django.contrib.auth import get_user_model
from product_app.models import Product
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_("کاربر"), on_delete=models.CASCADE, related_name="orders")
    date_created = models.DateTimeField(_("تاریخ ایجاد"), auto_now=False, auto_now_add=False, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE)
    count = models.IntegerField(_("تعداد"), default=1)
    paid_price = models.CharField(_("هزینه پرداختی"), max_length=100, blank=True, null=True)
    is_paid = models.BooleanField(_("وضعیت پرداخت") ,default=False)
    full_price = models.CharField(_("قیمت کل"), max_length=100, editable=False, blank=True, null=True)
    
    def full_price(self):
        return self.product.price * self.count
        
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = _("سبد خرید")
        verbose_name_plural = _("سبد خرید ها")


class PaidOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("سبد خرید"), on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), verbose_name=_("کاربر"), on_delete=models.CASCADE, related_name="orders_pay")
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE)
    count = models.IntegerField(_("تعداد"), default=1)
    pay = models.CharField(_("پرداختی"), max_length=100)
    full_name = models.CharField(_("نام و نام خانوادگی"), max_length=100)
    phone_number = models.CharField(_("شماره تلفن"), max_length=50)
    post_code = models.CharField(_("کد پستی"), max_length=50)
    address = models.TextField(_("آدرس"))
    tracking_code = models.CharField(_("کد رهگیری"), max_length=100, blank=True, null=True, help_text=_("باید ادمین پر کند"))
    date_created = models.DateTimeField(_("تاریخ ایجاد"), auto_now=False, auto_now_add=False, blank=True, null=True)
    status = models.BooleanField(_("پرداخت شده / نشده"), default=False)
    complete = models.BooleanField(_("ارسال شده / نشده"), default=False)
    
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = _("سفارشات موفق")
        verbose_name_plural = verbose_name

class BankPay(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_("کاربر"), on_delete=models.CASCADE, related_name="transactions")
    order = models.ForeignKey(PaidOrder, verbose_name=_("سبد خرید"), on_delete=models.CASCADE)
    code = models.IntegerField(_("کد وضعیت پرداختی"), default=None)
    ref_id = models.IntegerField(_("شماره تراکنش"), default=None)
    card_pan = models.TextField(_("شماره کارت به صورت ماسک"))
    card_hash = models.TextField(_("شماره کارت به صورت SHA256"))
    fee_type = models.CharField(_("پرداخت کننده کارمزد"), max_length=100)
    fee = models.IntegerField(_("کارمزد"), default=None)
    date_created = models.DateTimeField(_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    
    
    def __str__(self):
        return self.card_pan
    
    class Meta:
        verbose_name = _("تراکنش ها")
        verbose_name_plural = verbose_name