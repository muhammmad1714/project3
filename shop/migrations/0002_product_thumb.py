# Generated by Django 4.1.7 on 2023-07-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumb',
            field=models.ImageField(default='default.png', null=True, upload_to=''),
        ),
    ]
