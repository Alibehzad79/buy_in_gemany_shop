# Generated by Django 4.2.5 on 2023-10-16 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['-active', '-id'], 'verbose_name': 'اسلایدر', 'verbose_name_plural': 'اسلایدرها'},
        ),
    ]
