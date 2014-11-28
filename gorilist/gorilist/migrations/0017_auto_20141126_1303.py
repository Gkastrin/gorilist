# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gorilist', '0016_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='token',
            new_name='token_id',
        ),
    ]
