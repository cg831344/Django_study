# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_secondmodel_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondmodel',
            name='Date',
            field=models.DateField(default='2014-11-28'),
            preserve_default=False,
        ),
    ]
