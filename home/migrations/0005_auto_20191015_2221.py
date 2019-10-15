# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191015_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='totalraised',
            options={'verbose_name_plural': 'Total Raised'},
        ),
        migrations.AlterField(
            model_name='totalraised',
            name='money_raised',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
