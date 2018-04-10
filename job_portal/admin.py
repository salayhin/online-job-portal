# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import BusinessType
from .models import Company, Contract, Job, Faq

admin.site.register(BusinessType)
admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Job)
admin.site.register(Faq)


