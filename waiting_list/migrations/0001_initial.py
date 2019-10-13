# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-13 00:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0012_book_percentage_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('your_turn', models.BooleanField(default=False)),
                ('wl_book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_book', to='books.Book')),
                ('wl_user', models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
