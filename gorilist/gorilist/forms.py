__author__ = 'mpetyx'

from django import forms
from models import Note, Task, TaskList
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, ModelMultipleChoiceField, Form

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=250)
    body = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField(widget=SelectDateWidget )
    class Meta:
        model = Note

class TaskForm(forms.ModelForm):
    # importance = forms.CheckboxInput()
    title = forms.CharField(max_length=250)
    body = forms.CharField(widget=forms.Textarea)
    note = forms.ModelMultipleChoiceField(queryset=Note.objects.all(), required=False)
    pub_date = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Task

class TaskListForm(forms.ModelForm):
    task = forms.ModelMultipleChoiceField(queryset=Task.objects.all())
    title = forms.CharField(max_length=250)
    pub_date= forms.DateField(widget=SelectDateWidget)
    last_change = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = TaskList