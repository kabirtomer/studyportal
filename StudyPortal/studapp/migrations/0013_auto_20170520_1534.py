# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0012_remove_other_paper'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='minor1',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='minor2',
            name='paper',
        ),
        migrations.AddField(
            model_name='major',
            name='paper_real',
            field=models.FileField(default='none', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minor1',
            name='paper_real',
            field=models.FileField(default='none', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minor2',
            name='paper_real',
            field=models.FileField(default='none', upload_to=b''),
            preserve_default=False,
        ),
    ]
