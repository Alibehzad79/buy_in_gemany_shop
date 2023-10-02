from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(_("نام دسته بندی"), max_length=100, help_text=_("مثال: دسته بندی"))
    slug = models.SlugField(_("اسلاگ"), help_text=_("مثال: category-slug"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")

class Tag(models.Model):
    name = models.CharField(_("نام دسته بندی"), max_length=100, help_text=_("مثال: برچسب"))
    slug = models.SlugField(_("اسلاگ"), help_text=_("مثال: tag-slug"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("برچسب")
        verbose_name_plural = _("برچسب ها")
        
    
class Product(models.Model):
    STATUS = (
        ('avalible', 'موجود'),
        ('unavalible', 'ناموجود')
    )
    title = models.CharField(verbose_name=_('عنوان محصول'), max_length=100)
    slug = models.SlugField(_("اسلاگ"), help_text=_("product-name"))
    content = HTMLField(verbose_name=_("توضیحات محصول"))
    image = models.ImageField(_("تصویر محصول"), upload_to="images/products/")
    price = models.BigIntegerField(_("قیمت محصول"))
    delivery_time = models.IntegerField(_("مدت زمان تحویل"), help_text=_("مثال: 9 --> 9 روز کاری "), default=0)
    category = models.ForeignKey(Category, verbose_name=_("دسته بندی"), on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name=_("برچسب ها"))
    count = models.IntegerField(_("تعداد موجود در انبار"), default=0)
    status = models.CharField(_("وضعیت"), max_length=100, choices=STATUS, default='avalible')
    visit_count = models.IntegerField(_("تعداد بازدید"), default=0)
    
    def save(self, *args, **kwargs):
        if self.status == 'unavalible':
            self.count = 0
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.slug
    
    
    def get_absolute_url(self):
            return reverse("products_detail", kwargs={"pk": self.pk, 'slug': self.slug})
    
    class Meta:
        verbose_name = _("محصول")
        verbose_name_plural = _("محصولات")
        ordering = [
            '-id'
        ]
        
class Gallery(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE, related_name="galleries")
    title = models.CharField(_("عنوان تصویر"), max_length=100)
    image = models.ImageField(_("تصویر"), upload_to="images/galleries/")
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _("'تصویر'")
        verbose_name_plural = _("گالری")
class Comment(models.Model):
    STATUS = (
        ('pendding', 'در انتظار مشاهده'),
        ('accept', 'تایید شده'),
        ('reject', 'رد شده'),
    )
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(_("نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    text = models.TextField(_("نظر"))
    answre = models.TextField(_("جواب"))
    date_send = models.DateField(_("تاریخ ارسال"), auto_now=False, auto_now_add=False)
    status = models.CharField(_("وضعیت"), max_length=50, choices=STATUS, default='pendding')
    def __str__(self):
        return f"{self.email} ({self.get_status_display()})"
    
    class Meta:
        verbose_name = _("نظر")
        verbose_name_plural = _("نظرات")
        ordering = [
            '-date_send',
        ]