# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class PropertyList(models.Model):
    name = models.CharField(max_length=40)
    owner = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    location = models.CharField(max_length=15)
    image = models.CharField(null=True,max_length=40)

