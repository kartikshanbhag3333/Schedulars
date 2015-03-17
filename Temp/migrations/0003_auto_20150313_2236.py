# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Temp', '0002_to_do_list_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do_list',
            name='task_expected_time',
            field=models.CharField(default='x', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='to_do_list',
            name='task_in_time',
            field=models.CharField(default='x', max_length=100),
            preserve_default=False,
        ),
    ]
