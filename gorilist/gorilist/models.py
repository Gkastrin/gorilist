__author__ = 'mpetyx'


from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

class Task(models.Model):
    HIGH = 'HIGH'
    LOW ='LOW'
    AVERAGE = 'AVERAGE'
    PRIORITY_CHOICES=((HIGH,'High'),(LOW,'Low'),(AVERAGE,'Average'))
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True)
    dead_line = models.DateField('due date')
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES,default=AVERAGE)
    note = models.ManyToManyField(Note)
    pub_date = models.DateTimeField('date published')
    # finished =models.BooleanField()

    def __unicode__(self):
        return self.title

class TaskList(models.Model):
    title = models.CharField(max_length=250)
    task = models.ManyToManyField(Task)
    pub_date = models.DateTimeField('date published')
    last_change = models.DateTimeField('latest change')
    sessKey = models.CharField('session key',max_length=250)

    def __unicode__(self):
        return self.pk