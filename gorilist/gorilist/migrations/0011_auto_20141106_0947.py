# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0010_auto_20141106_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default=b'AV', max_length=2, choices=[(b'HI', b'High'), (b'LO', b'Low'), (b'AV', b'Average')]),
        ),
    ]
