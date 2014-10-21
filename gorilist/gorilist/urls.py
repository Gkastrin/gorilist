from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from django.views.generic import ListView
from models import TaskList, Note

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/$', views.NoteListView.as_view(), name='notes'),
    url(r'^tasks/$', views.TaskListView.as_view(), name='tasks'),
    url(r'^new_task_list/$', views.get_task_list, name='new_tasklist'),
    url(r'^new_task/$', views.get_task, name='new_task'),
    url(r'^new_task_list_task/$', views.get_task_list_task, name='new_task_list_task'),
    url(r'^new_task/(?P<t_l_id>\d+)/$', views.get_task, name='new_task'),
    url(r'^new_task_note/(?P<t_l_id>\d+)/$', views.get_task_note, name='new_note'),
    url(r'^remove_T_L/(?P<t_l_id>\d+)/$', views.remove_tasklist, name='remove task list'),
    url(r'^remove_T/(?P<t_id>\d+)/$', views.remove_task, name='remove task'),
    url(r'^remove_N/(?P<n_id>\d+)/$', views.remove_note, name='remove note'),
    url(r'^new_task_note/$', views.get_task_note, name='new_task_note'),
    url(r'^new_note/(?P<t_id>\d+)/$', views.get_note, name='new_note'),
    url(r'tasks/(?P<t_l_id>\d+)/$',views.taskspage, name="task_list"),
    url(r'^notes/(?P<t_id>\d+)/$', views.notespage, name="note_list" ),
    # url(r'^index_test/$', views.index, name='new index'),
)