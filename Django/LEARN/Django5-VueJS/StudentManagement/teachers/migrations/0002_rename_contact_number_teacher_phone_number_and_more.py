# Generated by Django 5.1 on 2024-09-17 12:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0003_alter_grade_options'),
        ('teachers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='contact_number',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='address',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birthday',
            field=models.DateField(help_text='格式例如：2020-05-01', verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='grades.grade', verbose_name='管理班级'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
