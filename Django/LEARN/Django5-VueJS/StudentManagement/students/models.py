from django.db import models
from django.contrib.auth.models import User
from grades.models import Grade

# Create your models here.
GENDER_CHOICES = [
    ('M', '男'),
    ('F', '女')
]


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_number = models.CharField(verbose_name='学籍号', max_length=20, unique=True)
    student_name = models.CharField(verbose_name='姓名', max_length=50)
    gender = models.CharField(verbose_name='性别', max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(verbose_name='出生日期', help_text='格式例如：2024-05-01')
    contact_number = models.CharField(verbose_name='联系方式', max_length=20)
    address = models.TextField(verbose_name="家庭住址")

    # 一对一关联
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 一个班级对应多个学生
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'student'
        verbose_name = '学生信息'
        verbose_name_plural = 'Student Information'
