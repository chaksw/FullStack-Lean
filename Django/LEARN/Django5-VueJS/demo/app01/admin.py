from django.contrib import admin
from app01.models import Article
# Register your models here.


# 自定义函数，返回外键的 username user.username
def get_author(obj):
    return obj.user.username


class ArticleAdmin(admin.ModelAdmin):
    # 将函数作为字段写入后台显示
    # django 会在使用 list_display 时给 get_author 传递 ArticleAdmin 的实例对象
    list_display = ('id', get_author, 'title', 'content', 'user')
    # 配置可供过滤的字段
    list_filter = ('title', 'content', 'user')
    # 配置搜索框，定义可供搜索的字段，注意外键不能作为可供搜索的字段
    search_fields = ('title', 'content')
    # 设置可跳转到详情页的字段
    list_display_links = ('id', 'title')
    # 设置直接修改功能
    list_editable = ('content',)


# 使用 short_description 将 get_author 的字段 header 更名为 'author'
get_author.short_description = 'author'
admin.site.register(Article, ArticleAdmin)
