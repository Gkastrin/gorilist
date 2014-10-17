__author__ = 'mpetyx'

import datetime
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import TaskList, Note, Task
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, ModelMultipleChoiceField, Form


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_task_list'

    def get_queryset(self):
        """Return the last twenty five published questions."""
        return TaskList.objects.order_by('-pub_date')[:25]


#### View for getting all the tasks of the database
class TaskListView(generic.ListView):
    template_name = 'tasks.html'
    model = Task


    def head(self, *args, **kwargs):
        task = self.get_queryset()
        response = HttpResponse('')
        response['Last-Modified'] = task.pub_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

###### View function for matching and presenting the tasks of a specific Task list, using its id
def taskspage(request, t_l_id):         # Present a list of all the tasks attached to the specified task list

    tasklist = TaskList.objects.get(id=t_l_id)
    result = []
    for task in tasklist.task.all():
         temp_task={}
         temp_task['id']=str(task.id)
         temp_task["title"]=str(task.title)
         temp_task["body"]=str(task.body)
         temp_task["pub_date"]=str(task.pub_date)
         result.append(temp_task)
    return render(request, "tasklist_tasks.html", {'result': result, 't_l_id':t_l_id})

#### View for getting all the notes of the database
class NoteListView(generic.ListView):
    template_name = 'notes.html'
    model = Note

    def head(self, *args, **kwargs):
        note = self.get_queryset()
        response = HttpResponse('')
        response['Last-Modified'] = note.pub_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

###### View function for matching and presenting the notes of a specific Task , using its id
def notespage(request, t_id):         # Present a list of all the notes attached to the specified task

    result=[]
    task = Task.objects.get(id=t_id)
    for note in task.note.all():
        temp_note={}
        temp_note['id']=str(note.id)
        temp_note['title']=str(note.title)
        temp_note['body']=str(note.body)
        temp_note['pub_date']=str(note.pub_date)
        result.append(temp_note)

    return render(request, "task_notes.html", {'result':result, 't_id': t_id})

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=250)
    body = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Note

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=250)
    body = forms.CharField(widget=forms.Textarea)
    note = forms.ModelMultipleChoiceField(queryset=Note.objects.all())
    pub_date = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Task

class TaskListForm(forms.ModelForm):
    task = forms.ModelMultipleChoiceField(queryset=Task.objects.all())
    pub_date= forms.DateField(widget=SelectDateWidget)
    last_change = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = TaskList


def get_task_list_task(request):
    t_l_id = None
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_task_list/')
    else:
        form = TaskForm()
    return render(request, "tasks_add.html", { 'form': form , 't_l_id':t_l_id})


def get_task_note(request, t_l_id=None):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            if t_l_id != None:
                return HttpResponseRedirect('/new_task/'+t_l_id)
            else:
                return HttpResponseRedirect('/new_task/')
    else:
        form = NoteForm()
    return render(request, "notes_add.html", { 'form' : form })

#### View function for creating and saving new note
def get_note(request, t_id=None):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            temp=form.save()
            if t_id!=None:
                task=Task.objects.get(id=t_id)
                task.note.add(temp)
                return HttpResponseRedirect('/notes/'+t_id)
            return HttpResponseRedirect('/new_task/')
    else:
        form = NoteForm()
    return render(request, "notes_add.html", { 'form' : form })

#### View function for creating and saving new task_list
def get_task_list(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskListForm
    return render(request, "task_list_add.html", {'form' : form})

#### View function for creating and saving new task
def get_task(request, t_l_id=None):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            temp = form.save()
            if t_l_id !=None:
                tasklist = TaskList.objects.get(id=t_l_id)
                tasklist.task.add(temp)
                return HttpResponseRedirect('/tasks/'+t_l_id)
            return HttpResponseRedirect('/new_task_list/')
    else:
        form = TaskForm()
    return render(request, "tasks_add.html", { 'form': form , 't_l_id':t_l_id})
