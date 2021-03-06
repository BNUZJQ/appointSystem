# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-02 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255, unique=True)),
                ('status',
                 models.IntegerField(choices=[(0, 'available'), (1, 'unavailable'), (2, 'repairing')], default=0)),
            ],
        ),
    ]
