# Generated by Django 4.0.4 on 2022-04-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_comments_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='email',
        ),
        migrations.AddField(
            model_name='comments',
            name='tel',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]
