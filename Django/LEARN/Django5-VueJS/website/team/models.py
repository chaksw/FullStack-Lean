from django.db import models

# Create your models here.


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    # upload_to 定义了 上传图片的相对路径，最终的上传路径为 settings.py 中定义的 MEDIA_ROOT 与这里定义路径拼接，如 'media/slide'
    avatar = models.ImageField('avatar name', upload_to='team', help_text='best size: 500x755')
    name = models.CharField('name', max_length=100)
    title = models.CharField('title', max_length=100)
    rank = models.IntegerField('order')

    class Meta:
        # 设置表名
        db_table = 'teams'
        verbose_name = "teams"
        verbose_name_plural = "teams"

    def __str__(self):
        return self.name
