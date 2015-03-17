# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Temp', '0005_auto_20150314_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_list',
            name='task_id',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
