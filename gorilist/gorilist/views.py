__author__ = 'mpetyx'

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from models import TaskList


class IndexView(generic.ListView):
    template_name = 'gorilist/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return TaskList.objects.order_by('-pub_date')[:5]

def page():

    return "Yo"

def notePage():

    return "Note Htaml"

def taskListPage():

    return "Task List Html"
