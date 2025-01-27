from django.contrib import admin
from blog.models import Category, Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author', 'counted_views', 'status', 'published_date', 'login_require','created_date', 'updated_date')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('post', 'name', 'created_date', 'active')
    list_filter = ('active', 'post')
    search_fields = ['message']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)