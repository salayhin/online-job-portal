# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BusinessType(models.Model):
    type = models.CharField(max_length=200)