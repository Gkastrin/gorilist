from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from django.views.generic import ListView
from models import TaskList

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^page(?P<num>[0-9]+)/$', views.page),

    (r'^lists/$', ListView.as_view(
        model=TaskList,
    )),

    (r'^notes/$', views.NoteListView.as_view()),


    url(r'note/add/$', views.NoteCreate.as_view(), name='note_add'),


)
