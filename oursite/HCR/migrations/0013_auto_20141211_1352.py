# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0012_auto_20141211_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 13, 52, 33, 577872, tzinfo=utc), verbose_name='appointment creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctorcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 13, 52, 33, 580168, tzinfo=utc), verbose_name='doctor comment creation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 13, 52, 33, 579592, tzinfo=utc), verbose_name='patient comment creation'),
            preserve_default=True,
        ),
    ]
