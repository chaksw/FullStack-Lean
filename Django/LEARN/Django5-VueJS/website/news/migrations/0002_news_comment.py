# Generated by Django 5.0.7 on 2024-08-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='comment',
            field=models.IntegerField(default=0, verbose_name='comment'),
        ),
    ]