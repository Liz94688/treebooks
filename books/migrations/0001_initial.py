# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-24 09:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('url_wiki', models.URLField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('book_img', models.ImageField(default='images/book.png', upload_to='images')),
                ('ISBN', models.CharField(default='', max_length=13)),
                ('publication_date', models.DateField(default=datetime.datetime.now)),
                ('summary', models.TextField()),
                ('format_book', models.CharField(choices=[('H', 'Hardcover'), ('P', 'Paperback')], max_length=1)),
                ('store', models.CharField(choices=[('1', 'Store1'), ('2', 'Store2')], max_length=1)),
                ('price_day', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pages', models.IntegerField(default=0)),
                ('avg_days', models.IntegerField(default=0)),
                ('language_book', models.CharField(default='', max_length=20)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('B', 'Biography'), ('N', 'Novel')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Category'),
        ),
    ]
