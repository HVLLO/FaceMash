from django.contrib import admin

from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
