# Generated by Django 4.1.3 on 2022-11-20 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferretic', '0014_product_product_enabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_enabled',
        ),
        migrations.RemoveField(
            model_name='sold',
            name='sold_enabled',
        ),
    ]
