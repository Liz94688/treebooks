# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-19 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_remove_book_current_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('street', models.CharField(max_length=15)),
                ('map_store', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.StoreBook'),
        ),
    ]
