# Generated by Django 4.2.5 on 2023-10-13 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0012_rename_pay_paidorder_payf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paidorder',
            old_name='payf',
            new_name='payfull',
        ),
    ]
