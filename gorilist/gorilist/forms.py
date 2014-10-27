__author__ = 'mpetyx'

from django import forms
from models import Note, Task, TaskList
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, ModelMultipleChoiceField, Form
from datetime import datetime

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=250)
    body = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    class Meta:
        model = Note

class TaskForm(forms.ModelForm):
    # importance = forms.CheckboxInput()
    title = forms.CharField(max_length=250)
    body = forms.CharField(widget=forms.Textarea)
    note = forms.ModelMultipleChoiceField(queryset=Note.objects.all(), required=False)
    pub_date = forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    class Meta:
        model = Task

class TaskListForm(forms.ModelForm):
    title = forms.CharField(max_length=250)
    task = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), required=False, widget=forms.HiddenInput)
    pub_date= forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    last_change = forms.DateTimeField( initial=datetime.now(), widget=forms.HiddenInput)
    class Meta:
        model = TaskList