# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0013_auto_20141106_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='note',
            field=models.ManyToManyField(to=b'gorilist.Note', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default=b'AVERAGE', max_length=7, choices=[(b'HIGH', b'High'), (b'LOW', b'Low'), (b'AVERAGE', b'Average')]),
        ),
    ]
