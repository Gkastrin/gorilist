# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0017_auto_20141126_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token_id',
            field=models.CharField(max_length=1000),
        ),
    ]
