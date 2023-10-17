from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core import validators
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(_("شماره موبایل"), unique=True, max_length=11, validators=[validators.MaxLengthValidator(11, 'شماره نباید بیشتر از 11 حرف باشه'), validators.MinLengthValidator(
        11, 'شماره نباید کمتر از 11 حرف باشد'), validators.RegexValidator('^(\\+98|0)?9\\d{9}$')], help_text=_("09123456789"))
    email = models.EmailField(_("ایمیل"), max_length=254, unique=True)
    reset_password_token = models.CharField(_("توکن بازیابی رمز"), max_length=256, blank=True, null=True, editable=True, unique=True)