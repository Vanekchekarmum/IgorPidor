# Generated by Django 4.0.4 on 2022-04-19 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_comments_approved_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='approved_comment',
            new_name='active',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='com',
        ),
        migrations.AddField(
            model_name='comments',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]
