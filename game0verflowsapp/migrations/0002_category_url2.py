# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game0verflowsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]