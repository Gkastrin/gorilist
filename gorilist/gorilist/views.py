__author__ = 'mpetyx'

from datetime import datetime
import requests
from django.forms.formsets import formset_factory
import json
import ast
from django.views import generic
from models import TaskList, Note, Task
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import string
from django.http import HttpResponseRedirect
from forms import NoteForm, TaskForm, TaskListForm, EditNForm, EditLForm, TokenForm, CloudNoteForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.sessions.models import Session

def infopage(request):
    return render(request,'info.html')

def contactpage(request):
    return render(request,'contact.html')

def cloudlet_note_delete(request, note_id, token):
    headers={"content-type":"application/json", "Authorization": str(token)}
    r=requests.delete('https://demo2.openi-ict.eu:443/api/v1/objects/'+str(note_id),headers=headers,verify=False)
    return HttpResponseRedirect('/notes/'+str(token))

def cloudlet_note_edit(request, note_id, token):
    if request.method == 'POST':
        form=CloudNoteForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data['text']
            title=form.cleaned_data['title']
            headers={'Authorization':str(token),'content-type':'application/json'}
            to_be_created ={
                "@openi_type":"t_fdf106cfb3e2658e838422ac6d5dde63-493",
                "@data":{
                    "text":str(text),
                    "title":str(title)
                }
            }
            r=requests.put('https://demo2.openi-ict.eu:443/api/v1/objects/'+str(note_id),headers=headers,verify=False,data=json.dumps(to_be_created))
            return HttpResponseRedirect('notes/'+str(token))
    else:
        form = CloudNoteForm()
        return render(request, 'cloud_note_edit.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            tok=form.cleaned_data['token_id']
            # us =form.cleaned_data['user']
            return HttpResponseRedirect('/notes/'+tok)
    else:
        form = TokenForm()
    return render(request, 'sign_in.html', {'form': form})

def index(request, token):

########################    CLOUDLET NOTES      #########################

    if request.method == 'POST':
        form = CloudNoteForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            title = form.cleaned_data['title']
            headers = {"Authorization":str(token),"content-type":"application/json"}
            to_be_created ={
                "@openi_type":"t_fdf106cfb3e2658e838422ac6d5dde63-493",
                "@data":{
                    "text":str(text),
                    "title":str(title)
                }
            }
            r=requests.post('https://demo2.openi-ict.eu:443/api/v1/objects' , data= json.dumps(to_be_created), headers=headers, verify=False)
            return HttpResponseRedirect('/notes/'+str(token))
    else:
        form= CloudNoteForm()
        headers= {'Authorization': str(token),'content-type':'application/json'}
        r= requests.get("https://demo2.openi-ict.eu:443/api/v1/objects", headers=headers, verify=False)
        temp = r.json()
        cloud_notes = []
        try:
            for note in temp['result']:
                no={}
                no['title']= str(note['@data']['title'])
                no['text']=str(note['@data']['text'])
                no['id']=str(note['@id'])
                cloud_notes.append(no)
                # l=len(cloud_notes)
        except:
            no = {}
        
        return render(request, 'index_new.html', {'token': token, 'cloud_notes': cloud_notes, 'form': form, 'temp':temp})

#########################################################################


#### View for getting all the tasks of the database
class TaskListView(generic.ListView):
    template_name = 'tasks.html'
    model = Task


    def head(self, *args, **kwargs):
        task = self.get_queryset()
        response = HttpResponse('')
        response['Last-Modified'] = task.pub_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

def user_logout(request):
    key = request.session.session_key
    tasklist = TaskList.objects.all()
    for t_l in tasklist:
        if t_l.sessKey == key:
            remove_tasklist(request, t_l.id)
    request.session.flush()
    return HttpResponseRedirect('/')

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
            if t_l_id is None:
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
            temp=form.save(commit=True)
            # print form
            if t_id is not None:
                task=Task.objects.get(id=t_id)
                task.note.add(temp)
                # return HttpResponseRedirect('/notes/'+t_id)
                return HttpResponseRedirect('/')
            # return HttpResponseRedirect('/new_task/')
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = NoteForm()
    return render(request, "notes_add.html", { 'form' : form })

##View function for editing a note
def edit_note(request, n_id):
    instance = Note.objects.get(id=n_id)
    form = NoteForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'note_edit.html', {'form': form})

###View function for editing a note
# def edit_note(request,n_id):
#     note = Note.objects.get(id=n_id)
#     form = EditNForm()
#     if request.method == 'POST':
#         form=EditNForm(request.POST)
#         if form.is_valid():
#             if form.cleaned_data['title'] :
#                 note.title=form.cleaned_data['title']
#             if form.cleaned_data['body'] :
#                 note.body=form.cleaned_data['body']
#             note.save()
#         return HttpResponseRedirect('/')
#     else:
#         form=EditNForm()
#     return render(request,'note_edit.html',{'form':form})


def edit_task(request, t_id):
    task = Task.objects.get(id=t_id)
    # instance ={'title':task.title,'body':task.body,'priority':task.priority }
    # form = EditTForm(initial={'title':task.title,'body':task.body,'priority':task.priority})
    form = TaskForm(request.POST or None, instance= task)
    # form = TaskForm(initial={'title':instance.title,'body':instance.body,'priority':instance.priority,'dead_line':instance.dead_line,'note':instance.note,'pub_date':instance.pub_date})
    if form.is_valid():
        # task.title=form.cleaned_data['title']
        # task.body=form.cleaned_data['body']
        # task.priority=form.cleaned_data['priority']
        form.save()
        return HttpResponseRedirect('/')
    return render(request,"task_edit.html",{'form':form})

###View function for editing a task
# def edit_task(request,t_id):
#     task = Task.objects.get(id=t_id)
#     if request.method == 'POST':
#         form=EditTForm(request.POST)
#         if form.is_valid():
#             if form.cleaned_data['title']:
#                 task.title=form.cleaned_data['title']
#             if form.cleaned_data['body']:
#                 task.body=form.cleaned_data['body']
#             if form.cleaned_data['priority']:
#                 task.priority=form.cleaned_data['priority']
#             if form.cleaned_data['dead_line']:
            #     task.dead_line=form.cleaned_data['dead_line']
            # task.save()
        # return HttpResponseRedirect('/')
    # else:
    #     form=EditTForm()
    # return render(request,'task_edit.html',{'form':form})


# def edit_task_list(request,t_l_id):
#     instance = TaskList.objects.get(id=t_l_id)
#     form = TaskListForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/')
#     return render(request, "task_list_edit.html", {'form':form})

### View function for editing a task list
def edit_task_list(request,t_l_id):
    tasklist = TaskList.objects.get(id=t_l_id)
    if request.method == 'POST':
        form = EditLForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['title']:
                tasklist.title=form.cleaned_data['title']
            tasklist.save()
        return HttpResponseRedirect('/')
    else:
        form=EditLForm()
    return render(request,'task_list_edit.html',{'form':form})

### View function for creating and saving new task_list
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
            if t_l_id is not None:
                tasklist = TaskList.objects.get(id=t_l_id)
                tasklist.task.add(temp)
                # return HttpResponseRedirect('/tasks/'+t_l_id)
                return HttpResponseRedirect('/')
            # return HttpResponseRedirect('/new_task_list/')
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()
    return render(request, "tasks_add.html", { 'form': form , 't_l_id':t_l_id})

def remove_tasklist(request, t_l_id):
    tasklist=TaskList.objects.get(id=t_l_id)
    for task in tasklist.task.all():
        for note in task.note.all():
            note.delete()
        task.delete()
    tasklist.delete()
    return HttpResponseRedirect('/')

def remove_task(request, t_id):
    task = Task.objects.get(id=t_id)
    for note in task.note.all():
        note.delete()
    task.delete()
    return HttpResponseRedirect('/')

def remove_note(request, n_id):
    note = Note.objects.get(id=n_id)
    note.delete()
    return HttpResponseRedirect('/')