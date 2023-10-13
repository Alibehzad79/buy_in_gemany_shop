# Generated by Django 4.2.5 on 2023-10-13 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order_app', '0009_paidorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidorder',
            name='address',
            field=models.TextField(default='', verbose_name='آدرس'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paidorder',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='ارسال شده / نشده'),
        ),
        migrations.AddField(
            model_name='paidorder',
            name='full_name',
            field=models.CharField(default='', max_length=100, verbose_name='نام و نام خانوادگی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paidorder',
            name='phone_number',
            field=models.CharField(default='', max_length=50, verbose_name='شماره تلفن'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paidorder',
            name='post_code',
            field=models.CharField(default='', max_length=50, verbose_name='کد پستی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paidorder',
            name='tracking_code',
            field=models.CharField(blank=True, help_text='باید ادمین پر کند', max_length=100, null=True, verbose_name='کد رهگیری'),
        ),
        migrations.AlterField(
            model_name='paidorder',
            name='status',
            field=models.BooleanField(default=False, verbose_name='پرداخت شده / نشده'),
        ),
        migrations.CreateModel(
            name='BankPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=None, verbose_name='کد وضعیت پرداختی')),
                ('ref_id', models.IntegerField(default=None, verbose_name='شماره تراکنش')),
                ('card_pan', models.TextField(verbose_name='شماره کارت به صورت ماسک')),
                ('card_hash', models.TextField(verbose_name='شماره کارت به صورت SHA256')),
                ('fee_type', models.CharField(max_length=100, verbose_name='پرداخت کننده کارمزد')),
                ('fee', models.IntegerField(default=None, verbose_name='کارمزد')),
                ('date_created', models.DateTimeField(verbose_name='تاریخ ایجاد')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.paidorder', verbose_name='سبد خرید')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'تراکنش ها',
                'verbose_name_plural': 'تراکنش ها',
            },
        ),
    ]
