# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_book_percentage_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='avg_days',
        ),
        migrations.RemoveField(
            model_name='book',
            name='language_book',
        ),
    ]
