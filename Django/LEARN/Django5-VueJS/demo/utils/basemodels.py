from django.db import models


class BaseModel(models.Model):
    # auto_now_add 自动填入目前时间
    # editable: 控制是否可编辑
    create_at = models.DateTimeField('createTime', auto_now_add=True, editable=True)
    update_at = models.DateTimeField('updateTime', auto_now_add=True, editable=True)

    # Base表只需要被继承，不需要创建在数据库中，所以设置元数据 abstract = True
    class Meta:
        abstract = True
