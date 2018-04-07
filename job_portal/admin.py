# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BusinessType
from .models import Company

from django.contrib import admin

# Register your models here.

admin.site.register(BusinessType)
admin.site.register(Company)