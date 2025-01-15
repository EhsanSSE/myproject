from django.contrib import admin
from main.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'created_date')
    search_fields = ['name', 'messsage']

admin.site.register(Contact, ContactAdmin)