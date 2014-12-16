# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0013_auto_20141211_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(verbose_name='appointment creation date', default=datetime.datetime(2014, 12, 12, 22, 58, 59, 379658, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctorcomment',
            name='date',
            field=models.DateTimeField(verbose_name='doctor comment creation', default=datetime.datetime(2014, 12, 12, 22, 58, 59, 381777, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientcomment',
            name='date',
            field=models.DateTimeField(verbose_name='patient comment creation', default=datetime.datetime(2014, 12, 12, 22, 58, 59, 381124, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
