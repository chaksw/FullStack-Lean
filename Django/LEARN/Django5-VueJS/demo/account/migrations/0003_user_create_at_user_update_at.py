# Generated by Django 5.0.7 on 2024-08-10 10:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_options_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='createTime'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='updateTime'),
            preserve_default=False,
        ),
    ]
