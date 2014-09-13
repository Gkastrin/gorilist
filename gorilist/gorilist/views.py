__author__ = 'mpetyx'

from django.views import generic
from models import TaskList, Note
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'gorilist/index.html'
    context_object_name = 'latest_task_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return TaskList.objects.order_by('-pub_date')[:5]

class NoteListView(generic.ListView):
    model = Note

    def head(self, *args, **kwargs):
        note = self.get_queryset()
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = note.pub_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

def page():

    return "Yo"

def notePage():

    return "Note Htaml"

def taskListPage():

    return "Task List Html"
