from django.db import models
from account.models import User
from utils.basemodels import BaseModel

# Create your models here.


class Article(BaseModel):
    class Meta:
        db_table = 'article'  # 设置表名
        verbose_name = 'articleInfo'  # 别名
        ordering = ['-publish_date']  # 以publish_date 降序， 发布越晚越靠前
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='title', max_length=120)
    content = models.TextField()
    publish_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
