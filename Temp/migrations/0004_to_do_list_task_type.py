# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Temp', '0003_auto_20150313_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do_list',
            name='task_type',
            field=models.CharField(default='x', max_length=100),
            preserve_default=False,
        ),
    ]
