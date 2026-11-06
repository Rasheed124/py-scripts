
from django.contrib import admin

from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "user__username")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "category",
        "priority",
        "completed",
        "due_date",
    )

    list_filter = (
        "completed",
        "priority",
        "category",
    )

    search_fields = (
        "title",
        "description",
        "user__username",
        "category__name",
    )
