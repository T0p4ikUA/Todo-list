from django.contrib import admin
from .models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "is_completed", "created_at")
    list_filter = ("is_completed", "tags")
    search_fields = ("title",)
    filter_horizontal = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
