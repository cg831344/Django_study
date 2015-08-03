# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_thirdmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdmodel',
            name='IP',
            field=models.IPAddressField(default='127.0.0.1'),
            preserve_default=False,
        ),
    ]
