# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-22 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0028_listfile_other_papers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listfile',
            name='other_papers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studapp.Other'),
        ),
    ]
