# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BusinessType,Company,Job,FAQ

from django.contrib import admin

# Register your models here.

admin.site.register(BusinessType)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(FAQ)