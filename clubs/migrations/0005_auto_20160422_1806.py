# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-22 23:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20160422_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='foundation',
            field=models.DateField(default=datetime.datetime(2016, 4, 22, 23, 6, 31, 157000, tzinfo=utc)),
        ),
    ]
