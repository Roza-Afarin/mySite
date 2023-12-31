from django.contrib import admin

# Register your models here.
from blog.models import post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    #fields = ('title',) if you want to restricked permission to change object's data in edit panel
    list_display = ('title','author','conted_vies','status','login_requier','published_date','created_date') 
    list_filter = ('status',)
    #ordering = ['-created_date'] #['created_date']
    search_fields = ['title','content','author']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','approved','created_date') 
    list_filter = ('approved',)
    #ordering = ['-created_date'] #['created_date']
    search_fields = ['name','post']
    summernote_fields = ('message',)

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(post,PostAdmin)