# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-22 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20191022_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default='', max_length=25),
        ),
    ]
