# Generated by Django 5.1 on 2024-08-29 14:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grades', '0002_alter_grade_options_alter_grade_grade_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_number', models.CharField(max_length=20, unique=True, verbose_name='学籍号')),
                ('student_name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=1, verbose_name='性别')),
                ('birthday', models.DateField(help_text='格式例如：2024-05-01', verbose_name='出生日期')),
                ('contact_number', models.CharField(max_length=20, verbose_name='联系方式')),
                ('address', models.TextField(verbose_name='家庭住址')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='grades.grade')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': 'Student Information',
                'db_table': 'student',
            },
        ),
    ]
