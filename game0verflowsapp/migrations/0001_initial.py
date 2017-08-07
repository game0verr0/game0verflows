# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('html_content', tinymce.models.HTMLField()),
                ('preview', models.TextField(max_length=225, null=True)),
                ('preview_img', models.ImageField(null=True, upload_to='upload/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game0verflowsapp.Category')),
                ('meta', models.ManyToManyField(to='game0verflowsapp.Meta')),
            ],
        ),
    ]