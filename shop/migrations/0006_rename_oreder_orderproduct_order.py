# Generated by Django 4.1.7 on 2023-08-09 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_orderproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='oreder',
            new_name='order',
        ),
    ]
