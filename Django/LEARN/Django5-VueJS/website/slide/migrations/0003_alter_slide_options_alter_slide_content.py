# Generated by Django 5.0.7 on 2024-08-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0002_alter_slide_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': 'slides', 'verbose_name_plural': 'slides'},
        ),
        migrations.AlterField(
            model_name='slide',
            name='content',
            field=models.CharField(help_text='heading 2', max_length=200, verbose_name='content'),
        ),
    ]
