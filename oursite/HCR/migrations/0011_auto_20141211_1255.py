# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0010_auto_20141211_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(verbose_name='appointment creation date', default=datetime.datetime(2014, 12, 11, 12, 55, 58, 575624, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctorcomment',
            name='date',
            field=models.DateTimeField(verbose_name='doctor comment creation', default=datetime.datetime(2014, 12, 11, 12, 55, 58, 577971, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientcomment',
            name='date',
            field=models.DateTimeField(verbose_name='patient comment creation', default=datetime.datetime(2014, 12, 11, 12, 55, 58, 577308, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
