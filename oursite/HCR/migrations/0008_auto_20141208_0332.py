# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0007_auto_20141208_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='a_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 3, 32, 17, 965694, tzinfo=utc), verbose_name='appointment creation date'),
            preserve_default=True,
        ),
    ]
