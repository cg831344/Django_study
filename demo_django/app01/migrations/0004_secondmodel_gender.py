# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_secondmodel_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondmodel',
            name='Gender',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
