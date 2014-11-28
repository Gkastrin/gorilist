# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0003_remove_tasklist_sesskey'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dead_line',
            field=models.DateTimeField(null=True, verbose_name=b'due date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default=b'A', max_length=1, null=True, choices=[(b'H', b'High'), (b'L', b'Low'), (b'A', b'Average')]),
            preserve_default=True,
        ),
    ]
