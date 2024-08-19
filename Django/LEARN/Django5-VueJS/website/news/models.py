from django.db import models
from datetime import datetime
# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=20)

    class Meta:
        db_table = 'categories'
        verbose_name = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class News(models.Model):
    id = models.AutoField(primary_key=True)
    cover = models.ImageField('cover', upload_to='news', blank=True, null=True, help_text='best size: 515x262')
    title = models.CharField('title', max_length=100)
    content = models.TextField('content')
    comment = models.IntegerField('comment', default=0)
    create_at = models.DateTimeField('create_time', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField('updated_time', auto_now_add=True, editable=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title
