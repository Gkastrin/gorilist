__author__ = 'mpetyx'

from django import forms
from models import Note, Task, TaskList
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, ModelMultipleChoiceField, Form
from django.contrib import sessions
from datetime import datetime

class TokenForm(forms.Form):
    token_id = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'autocomplete':'off'}))
    # user = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'autocomplete':'off'}))

class CloudNoteForm(forms.Form):
    title = forms.CharField(max_length=250)
    text = forms.CharField(widget= forms.Textarea)

class EditLForm(forms.ModelForm):
    class Meta:
        model=TaskList
        fields = ('title',)

class EditNForm(forms.ModelForm):
    title = forms.CharField(max_length=250,required=False)
    class Meta:
        model = Note
        fields =('title','body')

class EditTForm(forms.ModelForm):
    title = forms.CharField(max_length=250,required=False)
    body = forms.CharField( widget= forms.Textarea, required=False)
    class Meta:
        model = Task
        fields = ('title','body','priority')

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=250, widget= forms.TextInput(attrs={'placeholder':'Note title','autocomplete':'off'}))
    pub_date = forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    class Meta:
        model = Note
        fields = '__all__'

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=250, widget= forms.TextInput(attrs={'placeholder':'Task title','autocomplete':'off'}))
    body = forms.CharField( widget= forms.Textarea, required=False, )
    dead_line = forms.DateField(widget=SelectDateWidget)
    # priority = forms.ChoiceField()
    note = forms.ModelMultipleChoiceField(queryset=Note.objects.all(), required=False)
    pub_date = forms.DateTimeField(widget=forms.HiddenInput, initial=datetime.now())
    # finished = forms.BooleanField(widget=forms.HiddenInput, initial=False)
    class Meta:
        model = Task
        fields = '__all__'

class TaskListForm(forms.ModelForm):
    title = forms.CharField(max_length=250, widget= forms.TextInput(attrs={'placeholder':'Workflow title','autocomplete':'off'}))
    task = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), required=False, widget=forms.HiddenInput)
    pub_date= forms.DateTimeField( initial=datetime.now(), widget=forms.HiddenInput)
    last_change = forms.DateTimeField(initial=datetime.now(), widget=forms.HiddenInput)
    sessKey = forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model = TaskList
        fields ='__all__'