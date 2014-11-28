# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0011_auto_20141106_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='sessKey',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
