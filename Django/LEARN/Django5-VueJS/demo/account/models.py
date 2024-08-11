from django.db import models
from utils.basemodels import BaseModel
# Create your models here.


class User(BaseModel):
    class Meta:
        db_table = 'user'  # 表名
        verbose_name = 'userInfo'  # 别名
        verbose_name_plural = 'User Information'  # 后台模型名称
    # AutoField 自增
    id = models.AutoField(primary_key=True)
    # verbose_name： 别名，页面显示时的名字
    # null 控制是否允许在数据库上为空
    # blank 控制是否允许在页面显示时为空
    # unique 控制值是否唯一
    username = models.CharField(verbose_name='username', max_length=30, null=True, blank=True, unique=True)
    password = models.CharField(verbose_name='password', max_length=30)
    email = models.EmailField(verbose_name='email', null=True, blank=True, unique=True)

    # 设置 __str__, 当需要输出（显示）User 实例时，会自动调用，显示对应 return 的值
    def __str__(self):
        return self.username
