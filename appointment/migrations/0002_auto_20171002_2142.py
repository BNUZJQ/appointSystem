# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-02 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='custom',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='duration',
            field=models.CharField(choices=[(0, '0:00-1:00'), (1, '1:00-2:00')], max_length=10),
        ),
    ]
