# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-22 20:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20191021_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]