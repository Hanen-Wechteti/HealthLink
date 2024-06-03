from django.contrib import admin

from.models import Task 

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'list_date', 'nurse')
    list_display_links = ('id', 'title')
    list_filter = ('nurse',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'adress', 'city', 'state', )
    list_per_page = 25
admin.site.register(Task, TaskAdmin)
