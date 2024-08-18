from django.contrib import admin
from slide.models import Slide
# Register your models here.


class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_filter = ('title', 'content')
    search_fields = ('title', 'content')
    list_editable = ('title', 'content')


admin.site.register(Slide, SlideAdmin)
