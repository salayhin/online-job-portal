# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BusinessType,Company,Job,FAQ,Empolyee,Emp_education,Emp_experience

from django.contrib import admin

# Register your models here.

admin.site.register(BusinessType)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Faq)
admin.site.register(Empolyee)
admin.site.register(Emp_education)
admin.site.register(Emp_experience)