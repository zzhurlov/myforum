from django.contrib import admin
from forum.models import Topic, Post


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["topic", "message", "author", "publish"]
