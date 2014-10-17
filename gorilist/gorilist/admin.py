__author__ = 'mpetyx'


from models import Task, TaskList, Note
from django.contrib import admin

class NoteAdmin(admin.ModelAdmin):
    pass

class TaskListAdmin(admin.ModelAdmin):
    #list_display = ('publisher', 'pub_date', 'last_change')
    pass

class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Note, NoteAdmin)
