from django.contrib import admin
from news.models import Category, News

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('name',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'comment', 'created_at', 'category')
    list_filter = ('title', 'category')
    search_fields = ('title', 'category')
    list_editable = ('category', 'comment')


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
