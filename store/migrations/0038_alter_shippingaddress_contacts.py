# Generated by Django 4.0.4 on 2022-04-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_alter_shippingaddress_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='contacts',
            field=models.CharField(blank=True, default='whatsapp', max_length=80),
        ),
    ]
