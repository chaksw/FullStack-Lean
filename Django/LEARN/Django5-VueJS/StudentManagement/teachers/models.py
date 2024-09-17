from django.db import models
from django.contrib.auth.models import User
from grades.models import Grade

# Create your models here.
GENDER_CHOICES = [
    ('M', '男'),
    ('F', '女'),
]


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='teacher')
    teacher_name = models.CharField(verbose_name='姓名', max_length=50)
    phone_number = models.CharField(verbose_name='联系方式', max_length=20)
    gender = models.CharField(verbose_name='性别', max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(verbose_name='出生日期', help_text='格式例如：2020-05-01')
    grade = models.ForeignKey(to=Grade, verbose_name='管理班级', on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.teacher_name

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师信息'
        verbose_name_plural = 'Teacher Information'
