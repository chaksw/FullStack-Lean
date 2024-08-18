from django.contrib import admin
from team.models import Team
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'rank')
    list_filter = ('name', 'title')
    search_fields = ('name', 'title')
    list_editable = ('title', 'rank')


admin.site.register(Team, TeamAdmin)
