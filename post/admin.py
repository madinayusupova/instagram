from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'posted')
    list_filter = ('text', 'author', 'posted')
    search_fields = ('text', 'author',)
    raw_id_fields = ('author',)
    date_hierarchy = 'posted'
    ordering = ("posted", )
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('author', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('author', 'body')
