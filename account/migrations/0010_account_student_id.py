# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-16 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0009_auto_20171016_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='student_id',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
