# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0005_auto_20141105_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dead_line',
            field=models.DateField(verbose_name=b'due date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'H', b'High'), (b'L', b'Low'), (b'A', b'Average')]),
        ),
    ]
