from django.db import models

# Create your models here.


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    grade_name = models.CharField(verbose_name='班级名称', max_length=120, unique=True)
    grade_number = models.CharField(verbose_name='班级编号', max_length=10, unique=True)

    def __str__(self):
        return self.grade_name

    class Meta:
        db_table = 'grade'
        verbose_name = '班级'
        verbose_name_plural = 'Grade Information'
