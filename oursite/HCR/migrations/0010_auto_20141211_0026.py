# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0009_auto_20141209_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='doctor_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='patient_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='treatment',
            old_name='t_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='a_date',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 0, 26, 38, 561930, tzinfo=utc), verbose_name='appointment creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='validatedByPatient',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctorcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 0, 26, 38, 564015, tzinfo=utc), verbose_name='doctor comment creation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 0, 26, 38, 563482, tzinfo=utc), verbose_name='patient comment creation'),
            preserve_default=True,
        ),
    ]
