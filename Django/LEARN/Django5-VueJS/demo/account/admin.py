from django.contrib import admin
from account.models import User
# Register your models here.


# 创建 admin 数据模型， class 名字一般为 ModelNameAdmin
# 继承于 ModelAdmin 的类已经实现了 CRUD 功能
class UserAdmin(admin.ModelAdmin):
    # 定义显示显示在 admin 页面的字段
    list_display = ('id', 'username', 'email')
    # 配置可供过滤的字段
    list_filter = ('username', 'email')
    # 配置搜索框，定义可供搜索的字段
    search_fields = ('username', 'email')
    # 在当前 django 版本中 id 默认只读，所以 comment 掉
    # readonly_fields = ('id',)
    # 设置可跳转到详情页的字段
    list_display_links = ('id', 'username')
    # 设置直接修改功能
    list_editable = ('email',)


# 将数据模型与admin数据模型绑定
admin.site.register(User, UserAdmin)
