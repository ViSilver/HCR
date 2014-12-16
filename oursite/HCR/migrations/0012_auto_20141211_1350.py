# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0011_auto_20141211_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 13, 50, 17, 494227, tzinfo=utc), verbose_name='appointment creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctorcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 13, 50, 17, 496834, tzinfo=utc), verbose_name='doctor comment creation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 13, 50, 17, 496055, tzinfo=utc), verbose_name='patient comment creation'),
            preserve_default=True,
        ),
    ]
