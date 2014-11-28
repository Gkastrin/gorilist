# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0012_auto_20141106_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='sessKey',
            field=models.CharField(max_length=250, verbose_name=b'session key'),
        ),
    ]
