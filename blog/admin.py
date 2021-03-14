from django.contrib import admin
from .models import Blog, BlogComment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_author', 'blog_category', 'blog_title']


@admin.register(BlogComment)
class BlogComment(admin.ModelAdmin):
    list_display = ['comment_user', 'comment']
