# Generated by Django 4.0.4 on 2022-04-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_alter_shippingaddress_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='time',
            field=models.CharField(default='whatsapp', max_length=80),
        ),
    ]
