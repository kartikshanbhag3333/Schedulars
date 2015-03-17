# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('about', models.CharField(max_length=400)),
                ('image_path', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='To_Do_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=40)),
                ('task_name', models.CharField(max_length=400)),
                ('task_time', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
