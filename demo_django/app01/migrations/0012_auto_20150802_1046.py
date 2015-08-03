# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_authlist_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondmodel',
            name='Age',
            field=models.IntegerField(default=1, help_text=b'\xe4\xb8\x8d\xe8\xa6\x81\xe8\xb6\x85\xe8\xbf\x8710\xe5\xb2\x81'),
            preserve_default=True,
        ),
    ]
