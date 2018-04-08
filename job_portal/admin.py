# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import BusinessType
from .models import Company, Contract
from .models import Job
from .models import FAQ


admin.site.register(BusinessType)
admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Job)
admin.site.register(FAQ)

