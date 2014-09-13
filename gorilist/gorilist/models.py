__author__ = 'mpetyx'


from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

class Task(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    note = models.ManyToManyField(Note)
    pub_date = models.DateTimeField('date published')

class TaskList(models.Model):
    task = models.ManyToManyField(Task)
    pub_date = models.DateTimeField('date published')
    last_change = models.DateTimeField('latest change')

