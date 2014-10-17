from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from django.views.generic import ListView
from models import TaskList, Note

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/$', views.NoteListView.as_view(), name='notes'),
    url(r'^tasks/$', views.TaskListView.as_view(), name='tasks'),
    url(r'^new_task_list/$', views.get_task_list, name='new_tasklist'),
    url(r'^new_task/$', views.get_task, name='new_task'),
    url(r'^new_note/$', views.get_note, name='new_note'),
    ####Present the tasks of a specific task_list
    url(r'tasks/(?P<t_l_id>\d+)/$',views.taskspage, name="task_list"),
    ####Present the notes of a specific task
    url(r'^notes/(?P<t_id>\d+)/$', views.notespage, name="note_list" ),
)