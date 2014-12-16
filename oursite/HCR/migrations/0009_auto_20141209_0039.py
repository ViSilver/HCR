# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HCR', '0008_auto_20141208_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=2048)),
                ('date', models.DateTimeField(verbose_name='doctor comment creation', default=datetime.datetime(2014, 12, 9, 0, 39, 32, 886758, tzinfo=utc))),
                ('owner', models.ForeignKey(default=1, to='HCR.Doctor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=256)),
                ('owner', models.ForeignKey(default=1, to='HCR.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatientComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=2048)),
                ('date', models.DateTimeField(verbose_name='patient comment creation', default=datetime.datetime(2014, 12, 9, 0, 39, 32, 886223, tzinfo=utc))),
                ('owner', models.ForeignKey(default=1, to='HCR.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(default=1, to='HCR.Doctor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(default=1, to='HCR.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(default=1, to='HCR.Specialization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='a_date',
            field=models.DateTimeField(verbose_name='appointment creation date', default=datetime.datetime(2014, 12, 9, 0, 39, 32, 884704, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
