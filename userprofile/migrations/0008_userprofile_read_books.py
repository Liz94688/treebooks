# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-05 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_book_views'),
        ('userprofile', '0007_auto_20191003_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='read_books',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
