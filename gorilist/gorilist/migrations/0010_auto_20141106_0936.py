# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0009_auto_20141105_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='sessKey',
            field=models.CharField(default=b'session key', max_length=250, blank=True),
        ),
    ]
