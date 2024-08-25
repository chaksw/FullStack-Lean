from django.contrib import admin
from .models import Grade
# Register your models here.


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade_name', 'grade_number')


admin.site.register(Grade, GradeAdmin)
