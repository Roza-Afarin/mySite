from django.contrib import admin

# Register your models here.
from website.models import contact,Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','subject','created_date')
    list_filter = ('email',)
    search_fields = ('name','content')

admin.site.register(contact,ContactAdmin)
admin.site.register(Newsletter)

