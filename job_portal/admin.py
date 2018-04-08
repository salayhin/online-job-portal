# -*- coding: utf-8 -*-
from __future__ import unicode_literals
<<<<<<< HEAD
from .models import BusinessType
<<<<<<< HEAD
from .models import Company, Contract
=======
from .models import Company
from .models import Job
>>>>>>> 7328875c32bf7d7f6f9ac051d07ae1110e545384
=======
from .models import BusinessType,Company,Job,FAQ
>>>>>>> ff656bb0f74c0fe21a4e0e6ae2621643706d641e

from django.contrib import admin

# Register your models here.

admin.site.register(BusinessType)
admin.site.register(Company)
<<<<<<< HEAD
<<<<<<< HEAD
admin.site.register(Contract)
=======
admin.site.register(Job)
>>>>>>> 7328875c32bf7d7f6f9ac051d07ae1110e545384
=======
admin.site.register(Job)
admin.site.register(FAQ)
>>>>>>> ff656bb0f74c0fe21a4e0e6ae2621643706d641e
