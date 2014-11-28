# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0020_auto_20141126_1436'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Token',
        ),
    ]
