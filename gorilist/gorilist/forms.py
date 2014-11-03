__author__ = 'mpetyx'

from django import forms
from models import Note, Task, TaskList
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, ModelMultipleChoiceField, Form
from datetime import datetime

class EditLForm(forms.Form):
    title = forms.CharField(max_length=250, required=False)

class EditForm(forms.Form):
    title = forms.CharField(max_length=250,required=False)
    body = forms.CharField(widget=forms.Textarea, required=False)

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=250, widget= forms.TextInput(attrs={'placeholder':'Note title'}))
    body = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    class Meta:
        model = Note

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=250, widget= forms.TextInput(attrs={'placeholder':'Task title'}))
    body = forms.CharField( widget= forms.Textarea)
    note = forms.ModelMultipleChoiceField(queryset=Note.objects.all(), required=False, widget= forms.HiddenInput)
    pub_date = forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    class Meta:
        model = Task

class TaskListForm(forms.ModelForm):
    title = forms.CharField(max_length=250, widget= forms.TextInput(attrs={'placeholder':'Tasklist title'}))
    task = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), required=False, widget=forms.HiddenInput)
    pub_date= forms.DateTimeField( initial=datetime.now(), widget=forms.HiddenInput)
    last_change = forms.DateTimeField(initial=datetime.now(), widget=forms.HiddenInput)
    class Meta:
        model = TaskList