# Generated by Django 4.0.4 on 2022-04-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_alter_shippingaddress_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='pickup',
            field=models.CharField(default='доставка', max_length=80),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='time',
            field=models.CharField(max_length=80),
        ),
    ]