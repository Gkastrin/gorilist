# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0002_auto_20141105_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='sessKey',
        ),
    ]
