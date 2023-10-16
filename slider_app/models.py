from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Slider(models.Model):
    title = models.CharField(_("عنوان"), max_length=100)
    content = models.TextField(_("محتوا"), blank=True, null=True)
    url = models.URLField(_("لینک"), max_length=200, blank=True, null=True)
    image = models.ImageField(_("تصویر"), upload_to="images/sliders/")
    active = models.BooleanField(_("فعال / غیرغعال"), default=True)
    
    class Meta:
        verbose_name = _("اسلایدر")
        verbose_name_plural = verbose_name + _("ها")
        ordering = [
            '-active',
            '-id'
        ]

    def __str__(self):
        return self.title
    

# TODO this
