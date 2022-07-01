from django.contrib import admin
from .models import Todo, Task

# class TaskInLine(admin.TabularInline):
#     model = Task
#     extra = 1
class TaskInLine(admin.StackedInline):
    model = Task
    extra = 1

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority', 'is_done', 'todo_date', 'creation_time', 'update_time', 'my_custom_function_field')
    search_fields = ['name', 'description']
    list_filter = ['priority']
    fieldsets = (
        ("Maun Subtitle", {'fields': ['name', 'priority', 'is_done', 'my_custom_function_field']}),
        ("Date Information", {'fields': ['todo_date', 'creation_time', 'update_time']}),
        ("Description", {'fields': ['description']}),
    )
    inlines = [TaskInLine]
    readonly_fields = ["is_done", "creation_time", "update_time", "my_custom_function_field"]
    def my_custom_function_field(self, obj):
        task_names = ', '.join([_obj.name for _obj in obj.task_set.all()])
        return f"Task Names: {task_names}"
    my_custom_function_field.short_description = 'My Function'
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
# admin.site.register(Todo, TodoAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_filter = ('todo__is_done', 'todo__priority')
admin.site.register(Task, TaskAdmin)