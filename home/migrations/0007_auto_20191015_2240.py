# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_totalraised_number_books'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
    ]