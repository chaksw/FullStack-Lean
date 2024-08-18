from django.db import models

# Create your models here.


class Slide(models.Model):
    id = models.AutoField(primary_key=True)
    # upload_to 定义了 上传图片的相对路径，最终的上传路径为 settings.py 中定义的 MEDIA_ROOT 与这里定义路径拼接，如 'media/slide'
    image = models.ImageField('slide name', upload_to='slide', help_text='best size: 1920x1280')
    title = models.CharField('title', max_length=200, help_text='heading 1')
    content = models.CharField('content', max_length=200, help_text='heading 2')

    class Meta:
        # 设置表名
        db_table = 'slides'
        verbose_name = "slides"
        verbose_name_plural = "slides"
