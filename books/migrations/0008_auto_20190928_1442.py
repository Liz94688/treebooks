# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-28 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20190926_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='store',
            field=models.CharField(choices=[('Store1', 'Store1'), ('Store2', 'Store2')], max_length=15),
        ),
    ]
