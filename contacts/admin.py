from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task', 'email', 'contact_date')
    list_display_links =('id', 'name')
    search_fields = ('name', 'email', 'task')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)