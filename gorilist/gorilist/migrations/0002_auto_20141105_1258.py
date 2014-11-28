# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='sessKey',
            field=models.CharField(default=b'Session_Key', max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
