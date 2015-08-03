# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_colordic_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdmodel',
            name='IP2',
            field=models.GenericIPAddressField(null=True),
            preserve_default=True,
        ),
    ]
