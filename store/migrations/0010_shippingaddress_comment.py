# Generated by Django 4.0.4 on 2022-04-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_shippingaddress_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='comment',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
