# Generated by Django 5.1 on 2024-09-01 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_alter_grade_options_alter_grade_grade_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': '班级', 'verbose_name_plural': 'Grade Information'},
        ),
    ]
