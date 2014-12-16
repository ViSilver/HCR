# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0006_auto_20141208_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='a_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 3, 28, 46, 287911, tzinfo=utc), verbose_name='appointment creation date'),
            preserve_default=True,
        ),
    ]
