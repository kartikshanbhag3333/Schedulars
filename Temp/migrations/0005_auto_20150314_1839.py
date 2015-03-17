# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Temp', '0004_to_do_list_task_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_list',
            name='task_id',
            field=models.IntegerField(max_length=40),
            preserve_default=True,
        ),
    ]
