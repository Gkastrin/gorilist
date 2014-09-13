__author__ = 'mpetyx'


from models import Task, TaskList, Note
from django.contrib import admin

class NoteAdmin(admin.ModelAdmin):
    pass

class TaskListAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, NoteAdmin)
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Note, TaskAdmin)
