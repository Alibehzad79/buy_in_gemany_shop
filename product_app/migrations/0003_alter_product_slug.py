# Generated by Django 4.2.5 on 2023-10-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_alter_gallery_options_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='product-name', unique=True, verbose_name='اسلاگ'),
        ),
    ]