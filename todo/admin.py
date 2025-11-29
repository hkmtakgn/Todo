from django.contrib import admin

from todo.models import Task



@admin.register (Task)
class TaskAdmin (admin.ModelAdmin):
    list_display = [
        "task_name",
        "task_slug",
    ]

    