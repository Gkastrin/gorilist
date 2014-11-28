# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0006_auto_20141105_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='sessKey',
            field=models.CharField(max_length=250, null=True),
            preserve_default=True,
        ),
    ]
