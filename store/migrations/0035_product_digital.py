# Generated by Django 4.0.4 on 2022-04-25 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_category_remove_product_digital_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
