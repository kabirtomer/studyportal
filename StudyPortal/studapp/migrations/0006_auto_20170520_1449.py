# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0005_auto_20170520_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='sem',
            field=models.CharField(blank=True, help_text='Eg. 1', max_length=20),
        ),
        migrations.AlterField(
            model_name='document',
            name='year',
            field=models.CharField(blank=True, help_text='Eg. 2016-17', max_length=20),
        ),
    ]