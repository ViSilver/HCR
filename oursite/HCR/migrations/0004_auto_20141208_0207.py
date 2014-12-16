# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0003_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='validatedByPatient',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
