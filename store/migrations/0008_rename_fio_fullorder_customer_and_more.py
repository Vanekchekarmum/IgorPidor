# Generated by Django 4.0.4 on 2022-04-15 00:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_fullorder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fullorder',
            old_name='fio',
            new_name='customer',
        ),
        migrations.RemoveField(
            model_name='fullorder',
            name='adress',
        ),
        migrations.AddField(
            model_name='fullorder',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fullorder',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
