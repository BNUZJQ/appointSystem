# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-02 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]