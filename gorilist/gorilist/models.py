__author__ = 'mpetyx'


from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    note = models.ManyToManyField(Note)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

class TaskList(models.Model):
    title = models.TextField(max_length=250)
    task = models.ManyToManyField(Task)
    pub_date = models.DateTimeField('date published')
    last_change = models.DateTimeField('latest change')

    def __unicode__(self):
        return self.pk