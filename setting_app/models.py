from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.

class Setting(models.Model):
    site_name = models.CharField(_("نام سایت"), max_length=100)
    site_url = models.URLField(_("لینک سایت"), max_length=200, blank=True, null=True, help_text=_("https://..."))
    site_logo = models.ImageField(_("لوگوی سایت"), upload_to="images/logos/")
    about = HTMLField(_("درباره سایت"))
    owner = models.CharField(_("نام و نام خانوادگی صاحب سایت"), max_length=50)

    class Meta:
        verbose_name = _("تنظیمات")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.site_name


class Social(models.Model):
    setting = models.ForeignKey(Setting, verbose_name=_("تنظیمات"), on_delete=models.CASCADE, related_name="socials")
    name = models.CharField(_("نام شبکه"), max_length=100)
    url = models.URLField(_("لینک شبکه"), max_length=200, help_text=_("https://..."))
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("شبکه های اجتماعی")
        verbose_name_plural = verbose_name

class ContactUs(models.Model):
    full_name = models.CharField(_("نام و نام خانوادگی"), max_length=100)
    email = models.EmailField(_("ایمیل"), max_length=254)
    title = models.CharField(_("عنوان تماس"), max_length=100)
    text = models.TextField(_("نظر"))
    is_read = models.BooleanField(_("خوانده شده / نشده"), default=False)
    date_send = models.DateTimeField(_("تاریخ ارسال"), auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("تماس های کاربران")
        verbose_name_plural = verbose_name

class AboutUs(models.Model):
    setting = models.ForeignKey(Setting, verbose_name=_("تنظیمات"), on_delete=models.CASCADE, related_name="aboutus")
    title = models.CharField(_("عنوان"), max_length=100)
    description = HTMLField(_("توضیحات"))
    image = models.ImageField(_("تصویر"), upload_to="images/aboutus/", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("درباره ما")
        verbose_name_plural = verbose_name