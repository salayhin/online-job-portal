# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BusinessType,Company,Job,FAQ,Empolyee,Emp_education,Emp_experience


from django.contrib import admin
from .models import BusinessType
from .models import Company, Contract,Catagory
from .models import Job
from .models import Faq


admin.site.register(BusinessType)
admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Job)
admin.site.register(Faq)
admin.site.register(Empolyee)
admin.site.register(Emp_education)
admin.site.register(Emp_experience)
admin.site.register(Catagory)

