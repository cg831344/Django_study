# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondModel',
            fields=[
                ('Nid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'hanxin', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
