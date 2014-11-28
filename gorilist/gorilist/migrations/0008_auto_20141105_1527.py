# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0007_tasklist_sesskey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='sessKey',
            field=models.CharField(default=b'loulou', max_length=250),
        ),
    ]
