# Generated by Django 4.0.4 on 2022-04-22 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_shippingaddress_date_shippingaddress_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='contacts',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]
