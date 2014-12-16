# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0005_auto_20141208_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='a_date',
            field=models.DateTimeField(verbose_name='appointment creation date', default=datetime.datetime(2014, 12, 8, 3, 20, 42, 511538, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
