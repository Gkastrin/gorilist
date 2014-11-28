# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0014_auto_20141110_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='note',
            field=models.ManyToManyField(to=b'gorilist.Note'),
        ),
    ]
