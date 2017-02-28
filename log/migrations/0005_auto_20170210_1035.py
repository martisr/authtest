# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-10 08:35
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20170203_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='step',
            name='insertion_date',
            field=models.DateField(default=datetime.datetime(2017, 2, 7, 10, 35, 42, 374741)),
        ),
    ]