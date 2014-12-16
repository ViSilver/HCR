# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(verbose_name='creation date')),
                ('validatedByPatient', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
