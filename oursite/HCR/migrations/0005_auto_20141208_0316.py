# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0004_auto_20141208_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('t_date', models.DateTimeField(verbose_name='treatment creation date')),
                ('description', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.AddField(
            model_name='appointment',
            name='a_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 3, 16, 37, 170104, tzinfo=utc), verbose_name='appointment creation date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='treatment',
            field=models.OneToOneField(null=True, to='HCR.Treatment'),
            preserve_default=True,
        ),
    ]
