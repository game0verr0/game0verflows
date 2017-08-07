# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False)
    url = models.CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.name


class Meta(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False)
    date = models.DateField(auto_now=True, null=False)
    meta = models.ManyToManyField(Meta)

    html_content = HTMLField(null=False)
    category = models.ForeignKey(Category, null=False)

    preview = models.TextField(max_length=225, null=True)
    preview_img = models.ImageField(upload_to='static/upload/', null=True)

    def __unicode__(self):
        return self.title
