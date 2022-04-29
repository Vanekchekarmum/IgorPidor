# Generated by Django 4.0.4 on 2022-04-14 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_email_customer_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='compound',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
